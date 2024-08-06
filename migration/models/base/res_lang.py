# Copyright 2024 Ahmet Yiğit Budak (https://github.com/yibudak)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from migration import models_tree
from migration.libs.migration_mapper import BaseMapper, mapping


class ResLangMapper(BaseMapper):
    _name = "res.lang"
    _OLD_TABLE_NAME = "res_lang"
    _NEW_TABLE_NAME = "res_lang"

    @mapping
    def url_code(self, record):
        return {"url_code": record.get("iso_code")}


models_tree.add(ResLangMapper)
