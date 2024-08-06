# Copyright 2024 Ahmet Yiğit Budak (https://github.com/yibudak)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from migration import models_tree
from migration.libs.migration_mapper import BaseMapper, mapping


class ProductAttribute(BaseMapper):
    _name = "product.attribute"
    _OLD_TABLE_NAME = "product_attribute"
    _NEW_TABLE_NAME = "product_attribute"

    @mapping
    def display_type(self, record):
        # Radio is the default value for display_type in Odoo 16
        return {"display_type": "radio"}


models_tree.add(ProductAttribute)
