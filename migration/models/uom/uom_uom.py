# Copyright 2024 Ahmet Yiğit Budak (https://github.com/yibudak)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from migration import models_tree
from migration.libs.migration_mapper import BaseMapper, mapping


class UomUom(BaseMapper):
    _name = "uom.uom"
    _OLD_TABLE_NAME = "uom_uom"
    _NEW_TABLE_NAME = "uom_uom"


models_tree.add(UomUom)
