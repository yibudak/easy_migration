# Copyright 2024 Ahmet Yiğit Budak (https://github.com/yibudak)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from migration import models_tree
from migration.libs.migration_mapper import BaseMapper, mapping
from migration.libs.table_mapping import TABLE_MAPPING


class IrFilters(BaseMapper):
    _name = "ir.filters"
    _OLD_TABLE_NAME = "ir_filters"
    _NEW_TABLE_NAME = "ir_filters"


models_tree.add(IrFilters)
