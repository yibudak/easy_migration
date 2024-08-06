# Copyright 2024 Ahmet Yiğit Budak (https://github.com/yibudak)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from migration import models_tree
from migration.libs.migration_mapper import BaseMapper, mapping
from random import randint


class ProductAttributeValue(BaseMapper):
    _name = "product.attribute.value"
    _OLD_TABLE_NAME = "product_attribute_value"
    _NEW_TABLE_NAME = "product_attribute_value"

    @mapping
    def color(self, record):
        def _get_default_color(self):
            # Copied from odoo-server/addons/product/models/product_attribute.py:105
            return randint(1, 11)

        return {"color": _get_default_color(self)}


models_tree.add(ProductAttributeValue)
