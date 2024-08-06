# Copyright 2024 Ahmet Yiğit Budak (https://github.com/yibudak)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from migration import models_tree
from migration.libs.migration_mapper import BaseMapper, mapping


class ProductTemplateAttributeLine(BaseMapper):
    _name = "product.template.attribute.line"
    _OLD_TABLE_NAME = "product_template_attribute_line"
    _NEW_TABLE_NAME = "product_template_attribute_line"

    @mapping
    def active(self, record):
        return {"active": True}

    @mapping
    def value_count(self, record):
        return {"value_count": 0}


models_tree.add(ProductTemplateAttributeLine)
