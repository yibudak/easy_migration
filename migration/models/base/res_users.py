# Copyright 2024 Ahmet Yiğit Budak (https://github.com/yibudak)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from migration import models_tree
from migration.libs.migration_mapper import BaseMapper, mapping, join
from migration.libs.table_mapping import TABLE_MAPPING


class ResUsers(BaseMapper):
    _name = "res.users"
    _OLD_TABLE_NAME = "res_users"
    _NEW_TABLE_NAME = "res_users"

    @mapping
    def odoobot_failed(self, record):
        return {"odoobot_failed": None}

    @mapping
    def action_id(self, record):
        # Todo: maybe we can map action ids to new system
        return {"action_id": None}

    @mapping
    @join(
        table="res_users_authenticator",
        current_key="id",
        target_key="user_id",
        column="secret_key",
    )
    def totp_secret(self, record):
        if record["secret_key"]:
            return {"totp_secret": record["secret_key"][0]}
        else:
            return {"totp_secret": None}

    @mapping
    def notification_type_check(self, record):
        if record.get("share", False):
            return {"notification_type": "email"}
        else:
            return {}


models_tree.add(ResUsers)
