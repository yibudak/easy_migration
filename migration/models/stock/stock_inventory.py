# Copyright 2024 Ahmet Yiğit Budak (https://github.com/yibudak)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from migration import models_tree
from migration.libs.migration_mapper import BaseMapper, mapping


class StockInventory(BaseMapper):
    _name = "stock.inventory"
    _OLD_TABLE_NAME = "stock_inventory"
    _NEW_TABLE_NAME = "stock_inventory"


models_tree.add(StockInventory)