# Copyright 2024 Ahmet Yiğit Budak (https://github.com/yibudak)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from migration import models_tree
from migration.libs.migration_mapper import BaseMapper, mapping


class StockWarehouse(BaseMapper):
    _name = "stock.warehouse"
    _OLD_TABLE_NAME = "stock_warehouse"
    _NEW_TABLE_NAME = "stock_warehouse"

    @mapping
    def sequence(self, record):
        return {"sequence": 0}  # New Field

    @mapping
    def return_type_id(self, record):
        return {"return_type_id": None}  # New Field

    @mapping
    def delivery_steps(self, record):
        return {"manufacture_mto_pull_id": None}  # New Field


models_tree.add(StockWarehouse)
