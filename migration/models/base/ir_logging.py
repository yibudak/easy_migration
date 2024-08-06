# Copyright 2024 Ahmet Yiğit Budak (https://github.com/yibudak)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from migration import models_tree
from migration.libs.migration_mapper import BaseMapper, mapping


class IrLogging(BaseMapper):
    _name = "ir.logging"
    _OLD_TABLE_NAME = "ir_logging"
    _NEW_TABLE_NAME = "ir_logging"


models_tree.add(IrLogging)
