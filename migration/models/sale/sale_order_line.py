# Copyright 2024 Ahmet Yiğit Budak (https://github.com/yibudak)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from migration import models_tree
from migration.libs.migration_mapper import BaseMapper, mapping, join


class SaleOrderLine(BaseMapper):
    _name = "sale.order.line"
    _OLD_TABLE_NAME = "sale_order_line"
    _NEW_TABLE_NAME = "sale_order_line"

    @mapping
    def analytic_distribution(self, record):
        return {"analytic_distribution": None}

    @mapping
    def product_packaging_qty(self, record):
        return {"product_packaging_qty": None}

    @mapping
    def product_packaging_id(self, record):
        return {"product_packaging_id": None}


models_tree.add(SaleOrderLine)
