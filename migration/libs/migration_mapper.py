# Copyright 2024 Ahmet Yiğit Budak (https://github.com/yibudak)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from tqdm import tqdm
from migration.libs.exceptions import MissingFieldError
from migration.libs.helpers import (
    get_jsonb_columns,
    get_all_columns,
    read_table,
    insert_data,
    empty_table,
    get_total_row_count,
    convert_translated_fields,
    readable_number,
)
import logging


_logger = logging.getLogger(__name__)
_BATCH_SIZE = 5000


def mapping(func):
    func.is_mapping = True
    return func


def join(table, current_key, target_key, column):
    """
    Decorator to mark a method that requires a join.
    :param table: Target table to join.
    :param current_key: Key in the current table to join on.
    :param target_key: Key in the target table to join on.
    :param column: Column to fetch from the target table.
    """

    def decorator(func):
        if not hasattr(func, "_join_needs"):
            func._join_needs = []
        func._join_needs.append((table, current_key, target_key, column))
        return func

    return decorator


class BaseMapper(object):
    _name = "base.mapper"
    _order = ""
    _OLD_TABLE_NAME = "base_mapper"
    _NEW_TABLE_NAME = "base_mapper_new"
    _deleted_columns = {}

    def __init__(self, old_cursor, new_cursor, batch_size=_BATCH_SIZE):
        self.running_mode = None
        self.batch_size = batch_size
        self.old_cursor = old_cursor
        self.new_cursor = new_cursor
        self.old_columns = get_all_columns(
            self.old_cursor,
            self._OLD_TABLE_NAME,
        )
        self.new_columns = get_all_columns(
            self.new_cursor,
            self._NEW_TABLE_NAME,
        )
        self.translated_fields = get_jsonb_columns(
            self.new_cursor,
            self._NEW_TABLE_NAME,
        )
        self._build_mapping_methods()
        self._build_join_tree()

        self.order_by = self._build_order_by()
        self.total_records = get_total_row_count(
            cursor=self.old_cursor, table_name=self._OLD_TABLE_NAME
        )

        _logger.debug(
            "[%s] loaded with total %s columns, %s mapping methods, %s joins, %s records",
            self._name,
            len(self.old_columns),
            len(self._mapping_methods),
            len(self._join_tree),
            readable_number(self.total_records),
        )

    @classmethod
    def _build_mapping_methods(cls):
        mapping_methods = set()
        for name in dir(cls):
            attr = getattr(cls, name)
            if getattr(attr, "is_mapping", False):
                mapping_methods.add(name)
        cls._mapping_methods = mapping_methods

    @classmethod
    def _build_join_tree(cls):
        join_tree = {}
        for name in dir(cls):
            attr = getattr(cls, name)
            if hasattr(attr, "_join_needs"):
                for join_need in attr._join_needs:
                    table, current_key, target_key, column = join_need
                    if table not in join_tree:
                        join_tree[table] = {
                            "current_key": current_key,
                            "target_key": target_key,
                            "columns": [column],
                        }
                    else:
                        join_tree[table]["columns"].extend([column])
        cls._join_tree = join_tree

    @property
    def skip_processing(self):
        if self.total_records == 0:
            _logger.warning(
                "Skipping [%s] because there are no records in the table",
                self._OLD_TABLE_NAME,
            )
            return True
        else:
            return False

    def _build_order_by(self):
        if self._order:
            order_split = self._order.split(",")
            return tuple(
                [
                    [
                        x.strip().split(" ")[0],
                        (
                            x.strip().split(" ")[1]
                            if len(x.strip().split(" ")) > 1
                            else "ASC"
                        ),
                    ]
                ]
                for x in order_split
            )
        else:
            return tuple([[self.old_columns[0], "ASC"]])

    def analyze(self):

        if self.skip_processing:
            return

        self.running_mode = "analyze"
        _logger.info(
            "Analyzing [%s]...",
            self._OLD_TABLE_NAME,
        )
        single_record = read_table(
            cursor=self.old_cursor,
            table_name=self._OLD_TABLE_NAME,
            order_by=self.order_by,
            column_names=self.old_columns,
            limit=1,
            join_tree=self._join_tree,
        )
        mapped_data = self.map_data(single_record[0])
        if mapped_data:
            _logger.info("[OK] Analyze completed successfully.")
        else:
            _logger.error("[FAIL] Analyze failed for %s!", self._name)

    def migrate(self):
        if self.skip_processing:
            return

        self.running_mode = "migrate"
        empty_table(cursor=self.new_cursor, table_name=self._NEW_TABLE_NAME)
        with tqdm(
            total=self.total_records,
            desc="Migrating %s" % self._OLD_TABLE_NAME,
            unit=" record",
        ) as pbar:
            for offset in range(0, self.total_records, self.batch_size):
                old_data = read_table(
                    cursor=self.old_cursor,
                    table_name=self._OLD_TABLE_NAME,
                    order_by=self.order_by,
                    column_names=self.old_columns,
                    limit=self.batch_size,
                    offset=offset,
                    join_tree=self._join_tree,
                )
                # Insert new records
                for datum in old_data:
                    mapped_data = self.map_data(datum)

                    if self.translated_fields:
                        convert_translated_fields(
                            cursor=self.old_cursor,
                            table_name=self._OLD_TABLE_NAME,
                            jsonb_columns=self.translated_fields,
                            data_dict=mapped_data,
                        )

                    # Insert new records to res_country
                    insert_data(
                        cursor=self.new_cursor,
                        table_name=self._NEW_TABLE_NAME,
                        data=mapped_data,
                    )
                pbar.update(len(old_data))
        # self.new_cursor.connection.commit()
        return True

    def map_data(self, data):
        # Remove deleted columns
        if self._deleted_columns:
            for column in self._deleted_columns:
                data.pop(column, None)

        mapped_data = {}
        for column in self.new_columns:
            if column in data.keys():
                mapped_data[column] = data[column]
            else:
                continue

        # Evaluate mapping functions
        update_dict = self.eval_mapper_functions(data)
        if update_dict:
            mapped_data.update(update_dict)
        missing_fields = set(self.new_columns) - set(mapped_data.keys())

        if missing_fields:
            _logger.warning(
                "Missing fields in %s: %s",
                self._NEW_TABLE_NAME,
                missing_fields,
            )
            if self.running_mode == "migrate":
                raise MissingFieldError(self._name, missing_fields)

            return False

        return mapped_data

    def eval_mapper_functions(self, data):
        update_dict = {}
        for method in self._mapping_methods:
            vals = getattr(self, method)(data)
            if vals:
                update_dict.update(vals)

        return update_dict
