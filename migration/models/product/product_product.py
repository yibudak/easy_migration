# Copyright 2024 Ahmet Yiğit Budak (https://github.com/yibudak)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from migration import models_tree
from migration.libs.migration_mapper import BaseMapper, mapping


class ProductProduct(BaseMapper):
    _name = "product.product"
    _OLD_TABLE_NAME = "product_product"
    _NEW_TABLE_NAME = "product_product"

    @mapping
    def can_image_variant_1024_be_zoomed(self, record):
        return {"can_image_variant_1024_be_zoomed": None}

    @mapping
    def combination_indices(self, record):
        return {"combination_indices": None}


models_tree.add(ProductProduct)
