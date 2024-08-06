# Copyright 2024 Ahmet Yiğit Budak (https://github.com/yibudak)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from migration import models_tree
from migration.libs.migration_mapper import BaseMapper, mapping, join


class UTMCampaign(BaseMapper):
    _name = "utm.campaign"
    _OLD_TABLE_NAME = "utm_campaign"
    _NEW_TABLE_NAME = "utm_campaign"

    @mapping
    def stage_id(self, record):
        return {"stage_id": 1}  # default stage, required

    @mapping
    def user_id(self, record):
        return {"user_id": 1}  # OdooBot, required

    @mapping
    def company_id(self, record):
        return {"company_id": None}

    @mapping
    def title(self, record):
        return {"title": record.get("name")}

    @mapping
    def color(self, record):
        return {"color": None}

    @mapping
    def is_auto_campaign(self, record):
        return {"is_auto_campaign": False}  # default value


models_tree.add(UTMCampaign)
