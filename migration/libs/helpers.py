# Copyright 2024 Ahmet Yiğit Budak (https://github.com/yibudak)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from psycopg.types.json import Jsonb


def readable_number(number):
    number_str = str(number)[::-1]
    formatted_str = ".".join(
        [number_str[i : i + 3] for i in range(0, len(number_str), 3)]
    )
    return formatted_str[::-1]


def read_table(
    cursor, table_name, column_names, order_by=None, limit=-1, offset=-1, join_tree=None
):
    """
    Read table content entirely as python list of dictionaries, with necessary joins.
    """

    def quote_identifier(identifier):
        return f'"{identifier}"'

    quoted_table_name = quote_identifier(table_name)
    select_clauses = [f"{quoted_table_name}.*"]
    join_clauses = []
    group_by_clauses = [
        f"{quoted_table_name}.{quote_identifier(column)}" for column in column_names
    ]

    if join_tree:
        for table, join_info in join_tree.items():
            quoted_table = quote_identifier(table)
            current_key = quote_identifier(join_info["current_key"])
            target_key = quote_identifier(join_info["target_key"])
            columns = join_info["columns"]
            join_clause = f"LEFT JOIN {quoted_table} ON {quoted_table_name}.{current_key} = {quoted_table}.{target_key}"
            join_clauses.append(join_clause)

            for column in columns:
                quoted_column = quote_identifier(column)
                array_agg_clause = (
                    f"array_agg({quoted_table}.{quoted_column}) AS {quoted_column}"
                )
                select_clauses.append(array_agg_clause)

    base_query = f"SELECT {', '.join(select_clauses)} FROM {quoted_table_name}"
    if join_clauses:
        base_query += " " + " ".join(join_clauses)

    group_by_clause = f" GROUP BY {', '.join(group_by_clauses)}"
    query = base_query + group_by_clause

    if order_by:
        # Split order_by into columns and directions, quote only the column names
        order_by_clause = ", ".join(
            f"{quoted_table_name}.{quote_identifier(column)} {direction}"
            for column, direction in order_by
        )
        query += f" ORDER BY {order_by_clause}"
    if limit > 0:
        query += f" LIMIT {limit}"
    if offset > 0:
        query += f" OFFSET {offset}"

    cursor.execute(query)
    columns = [column[0] for column in cursor.description]
    result = []

    for row in cursor.fetchall():
        row_dict = dict(zip(columns, row))
        for vals in join_tree.values():
            for col in vals["columns"]:
                row_dict[col] = None if row_dict[col] == [None] else row_dict[col]
        result.append(row_dict)

    return result


def reset_sequence(cursor, table_name, column_name):
    cursor.execute(
        f"SELECT setval(pg_get_serial_sequence('{table_name}', '{column_name}'),"
        f" coalesce(max({column_name}), 1),"
        f" max({column_name}) IS NOT NULL) FROM {table_name};"
    )
    return True


def empty_table(cursor, table_name):
    # assert table_name in cursor.table_names(), "Table %s does not exist" % table_name
    delete_table = f"DELETE FROM {table_name} CASCADE"
    cursor.execute(delete_table)
    return True


def insert_data(cursor, table_name, data):
    columns = data.keys()
    values = data.values()
    query = f"""
    INSERT INTO {table_name}
    ({", ".join(columns)})
    VALUES ({", ".join(["%s"] * len(columns))})
    ON CONFLICT DO NOTHING
    """
    cursor.execute(query, list(values))
    return True


def get_total_row_count(cursor, table_name):
    query = f"SELECT COUNT(*) FROM {table_name}"
    cursor.execute(query)
    return cursor.fetchone()[0]


def get_all_columns(cursor, table_name):
    query = f"""
    SELECT column_name
    FROM information_schema.columns
    WHERE table_name = %s
    """
    cursor.execute(query, (table_name,))
    return [row[0] for row in cursor.fetchall()]


def get_jsonb_columns(cursor, table_name):
    """
    PostgreSQL-specific query to find jsonb columns
    """
    query = """
    SELECT column_name
    FROM information_schema.columns
    WHERE table_name = %s AND data_type = 'jsonb'
    """
    cursor.execute(query, (table_name,))
    return [row[0] for row in cursor.fetchall()]


def convert_translated_fields(cursor, table_name, jsonb_columns, data_dict):
    """
    Find field translations in ir.translation table and convert them into jsonb
    """
    model_name = table_name.replace("_", ".")
    for column_name in jsonb_columns:
        # Find translations
        query = """
        SELECT lang, value
        FROM ir_translation
        WHERE name = %s AND type = 'model' AND res_id = %s
        """
        cursor.execute(query, (f"{model_name},{column_name}", data_dict["id"]))
        translations = cursor.fetchall()
        if translations:
            # Convert translations to jsonb
            translation_dict = {}
            for tr in translations:
                translation_dict[tr[0]] = tr[1]
                if tr[0] == "en_US":
                    translation_dict["en_US"] = data_dict.get(column_name, "")
            data_dict[column_name] = Jsonb(translation_dict)
        else:
            data_dict[column_name] = Jsonb({"en_US": data_dict.get(column_name, "")})
