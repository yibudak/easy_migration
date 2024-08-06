# Copyright 2024 Ahmet Yiğit Budak (https://github.com/yibudak)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from migration import models_tree
from migration.libs.migration_mapper import BaseMapper, mapping


class MailActivity(BaseMapper):
    _name = "mail.activity"
    _OLD_TABLE_NAME = "mail_activity"
    _NEW_TABLE_NAME = "mail_activity"


models_tree.add(MailActivity)
