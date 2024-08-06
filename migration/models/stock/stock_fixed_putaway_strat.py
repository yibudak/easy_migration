# Copyright 2024 Ahmet Yiğit Budak (https://github.com/yibudak)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from migration import models_tree
from migration.libs.migration_mapper import BaseMapper, mapping


class StockFixedPutawayStrat(BaseMapper):
    _name = "stock.fixed.putaway.strat"
    _OLD_TABLE_NAME = "stock_fixed_putaway_strat"
    _NEW_TABLE_NAME = "stock_fixed_putaway_strat"


models_tree.add(StockFixedPutawayStrat)
