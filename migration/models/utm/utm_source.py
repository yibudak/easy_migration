# Copyright 2024 Ahmet Yiğit Budak (https://github.com/yibudak)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from migration import models_tree
from migration.libs.migration_mapper import BaseMapper, mapping, join


class UTMSource(BaseMapper):
    _name = "utm.source"
    _OLD_TABLE_NAME = "utm_source"
    _NEW_TABLE_NAME = "utm_source"


models_tree.add(UTMSource)
