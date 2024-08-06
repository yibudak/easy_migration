# Copyright 2024 Ahmet Yiğit Budak (https://github.com/yibudak)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from migration import models_tree
from migration.libs.migration_mapper import BaseMapper, mapping, join


class UTMMedium(BaseMapper):
    _name = "utm.medium"
    _OLD_TABLE_NAME = "utm_medium"
    _NEW_TABLE_NAME = "utm_medium"


models_tree.add(UTMMedium)
