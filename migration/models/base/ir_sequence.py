# Copyright 2024 Ahmet Yiğit Budak (https://github.com/yibudak)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from migration import models_tree
from migration.libs.migration_mapper import BaseMapper, mapping


class IrSequence(BaseMapper):
    _name = "ir.sequence"
    _OLD_TABLE_NAME = "ir_sequence"
    _NEW_TABLE_NAME = "ir_sequence"


models_tree.add(IrSequence)
