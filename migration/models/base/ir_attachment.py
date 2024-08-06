# Copyright 2024 Ahmet Yiğit Budak (https://github.com/yibudak)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from migration import models_tree
from migration.libs.migration_mapper import BaseMapper, mapping
from migration.libs.table_mapping import TABLE_MAPPING


class IrAttachment(BaseMapper):
    _name = "ir.attachment"
    _OLD_TABLE_NAME = "ir_attachment"
    _NEW_TABLE_NAME = "ir_attachment"

    @mapping
    def res_model(self, record):
        if record.get("res_model") in TABLE_MAPPING.keys():
            return {"res_model": TABLE_MAPPING[record.get("res_model")]}
        else:
            return {}

    @mapping
    def original_id(self, record):
        return {"original_id": None}


models_tree.add(IrAttachment)
