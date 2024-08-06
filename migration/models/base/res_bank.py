# Copyright 2024 Ahmet Yiğit Budak (https://github.com/yibudak)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from migration import models_tree
from migration.libs.migration_mapper import BaseMapper, mapping


class ResBankMapper(BaseMapper):
    _name = "res.bank"
    _OLD_TABLE_NAME = "res_bank"
    _NEW_TABLE_NAME = "res_bank"


models_tree.add(ResBankMapper)
