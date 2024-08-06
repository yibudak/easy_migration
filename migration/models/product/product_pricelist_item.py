# Copyright 2024 Ahmet Yiğit Budak (https://github.com/yibudak)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from migration import models_tree
from migration.libs.migration_mapper import BaseMapper, mapping


class ProductPricelistItem(BaseMapper):
    _name = "product.pricelist.item"
    _OLD_TABLE_NAME = "product_pricelist_item"
    _NEW_TABLE_NAME = "product_pricelist_item"

    @mapping
    def active(self, record):
        # Related to pricelist_id.active
        return {"active": None}


models_tree.add(ProductPricelistItem)
