# Copyright 2024 Ahmet Yiğit Budak (https://github.com/yibudak)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from migration import models_tree
from migration.libs.migration_mapper import BaseMapper, mapping


class UomCategory(BaseMapper):
    _name = "uom.category"
    _OLD_TABLE_NAME = "uom_category"
    _NEW_TABLE_NAME = "uom_category"


models_tree.add(UomCategory)
