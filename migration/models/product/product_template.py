# Copyright 2024 Ahmet Yiğit Budak (https://github.com/yibudak)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from migration import models_tree
from migration.libs.migration_mapper import BaseMapper, mapping


class ProductTemplate(BaseMapper):
    _name = "product.template"
    _OLD_TABLE_NAME = "product_template"
    _NEW_TABLE_NAME = "product_template"

    @mapping
    def can_image_1024_be_zoomed(self, record):
        return {"can_image_1024_be_zoomed": None}

    @mapping
    def has_configurable_attributes(self, record):
        return {"has_configurable_attributes": None}

    @mapping
    def detailed_type(self, record):
        return {"detailed_type": record.get("type")}

    @mapping
    def days_to_prepare_mo(self, record):
        return {"days_to_prepare_mo": 0.0}

    @mapping
    def priority(self, record):
        return {"priority": "0"}


models_tree.add(ProductTemplate)
