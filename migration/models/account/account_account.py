# Copyright 2024 Ahmet Yiğit Budak (https://github.com/yibudak)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from migration import models_tree
from migration.libs.migration_mapper import BaseMapper, mapping


class AccountAccount(BaseMapper):
    _name = "account.account"
    _OLD_TABLE_NAME = "account_account"
    _NEW_TABLE_NAME = "account_account"


models_tree.add(AccountAccount)