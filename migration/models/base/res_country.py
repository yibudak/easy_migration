# Copyright 2024 Ahmet Yiğit Budak (https://github.com/yibudak)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from migration import models_tree
from migration.libs.migration_mapper import BaseMapper, mapping


class ResCountryMapper(BaseMapper):
    _name = "res.country"
    _OLD_TABLE_NAME = "res_country"
    _NEW_TABLE_NAME = "res_country"

    @mapping
    def state_required(self, record):
        return {"state_required": True}

    @mapping
    def zip_required(self, record):
        return {"zip_required": True}


models_tree.add(ResCountryMapper)
