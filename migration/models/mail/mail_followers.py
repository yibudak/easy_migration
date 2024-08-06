# Copyright 2024 Ahmet Yiğit Budak (https://github.com/yibudak)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from migration import models_tree
from migration.libs.migration_mapper import BaseMapper, mapping


class MailFollowers(BaseMapper):
    _name = "mail.followers"
    _OLD_TABLE_NAME = "mail_followers"
    _NEW_TABLE_NAME = "mail_followers"


models_tree.add(MailFollowers)
