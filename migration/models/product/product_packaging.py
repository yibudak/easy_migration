# Copyright 2024 Ahmet Yiğit Budak (https://github.com/yibudak)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from migration import models_tree
from migration.libs.migration_mapper import BaseMapper, mapping


class ProductPackaging(BaseMapper):
    _name = "product.packaging"
    _OLD_TABLE_NAME = "product_packaging"
    _NEW_TABLE_NAME = "product_packaging"


models_tree.add(ProductPackaging)
