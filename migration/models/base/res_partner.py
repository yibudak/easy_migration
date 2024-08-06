# Copyright 2024 Ahmet Yiğit Budak (https://github.com/yibudak)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from migration import models_tree
from migration.libs.migration_mapper import BaseMapper, mapping
from migration.libs.table_mapping import TABLE_MAPPING


class ResPartner(BaseMapper):
    _name = "res.partner"
    _OLD_TABLE_NAME = "res_partner"
    _NEW_TABLE_NAME = "res_partner"

    @mapping
    def company_registry(self, record):
        return {"company_registry": None}

    @mapping
    def email_normalized(self, record):
        return {"email_normalized": None}

    @mapping
    def supplier_rank(self, record):
        return {"supplier_rank": None}

    @mapping
    def customer_rank(self, record):
        return {"customer_rank": record.get("ranking")}  # Altinkaya custom field

    @mapping
    def partner_longitude(self, record):
        return {"partner_longitude": None}

    @mapping
    def partner_latitude(self, record):
        return {"partner_latitude": None}


models_tree.add(ResPartner)
