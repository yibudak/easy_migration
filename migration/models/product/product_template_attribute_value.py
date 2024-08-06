# Copyright 2024 Ahmet Yiğit Budak (https://github.com/yibudak)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from migration import models_tree
from migration.libs.migration_mapper import BaseMapper, mapping
from random import randint


class ProductTemplateAttributeValue(BaseMapper):
    _name = "product.template.attribute.value"
    _OLD_TABLE_NAME = "product_template_attribute_value"
    _NEW_TABLE_NAME = "product_template_attribute_value"

    @mapping
    def color(self, record):
        def _get_default_color(self):
            # Copied from odoo-server/addons/product/models/product_attribute.py:105
            return randint(1, 11)

        return {"color": _get_default_color(self)}

    @mapping
    def ptav_active(self, record):
        return {"active": True}

    @mapping
    def ptav_value_count(self, record):
        return {"value_count": 0}

    # TODO: Map missing fields.


models_tree.add(ProductTemplateAttributeValue)
