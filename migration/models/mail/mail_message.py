# Copyright 2024 Ahmet Yiğit Budak (https://github.com/yibudak)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from migration import models_tree
from migration.libs.migration_mapper import BaseMapper, mapping


class MailMessage(BaseMapper):
    _name = "mail.message"
    _OLD_TABLE_NAME = "mail_message"
    _NEW_TABLE_NAME = "mail_message"

    @mapping
    def is_internal(self, record):
        return {"is_internal": None}

    @mapping
    def email_layout_xmlid(self, record):
        return {"email_layout_xmlid": None}

    @mapping
    def email_add_signature(self, record):
        return {"email_add_signature": True}  # default value

    @mapping
    def reply_to_force_new(self, record):
        return {"reply_to_force_new": None}

    @mapping
    def author_guest_id(self, record):
        return {"author_guest_id": None}


models_tree.add(MailMessage)
