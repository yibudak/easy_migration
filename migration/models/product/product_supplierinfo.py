# Copyright 2024 Ahmet Yiğit Budak (https://github.com/yibudak)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from migration import models_tree
from migration.libs.migration_mapper import BaseMapper, mapping


class ProductSupplierinfo(BaseMapper):
    _name = "product.supplierinfo"
    _OLD_TABLE_NAME = "product_supplierinfo"
    _NEW_TABLE_NAME = "product_supplierinfo"

    @mapping
    def partner_id(self, record):
        return {"partner_id": record.get("name")}


models_tree.add(ProductSupplierinfo)
