# Copyright 2024 Ahmet Yiğit Budak (https://github.com/yibudak)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from migration import models_tree
from migration.libs.migration_mapper import BaseMapper, mapping, join


class SaleOrder(BaseMapper):
    _name = "sale.order"
    _OLD_TABLE_NAME = "sale_order"
    _NEW_TABLE_NAME = "sale_order"

    @mapping
    def signed_on(self, record):
        return {"signed_on": record.get("signed_on")}

    @mapping
    def project_id(self, record):
        return {"project_id": None}

    @mapping
    def incoterm_location(self, record):
        return {"incoterm_location": None}

    @mapping
    def delivery_status(self, record):
        return {"delivery_status": None}

    @mapping
    @join(
        table="product_pricelist",
        current_key="pricelist_id",
        target_key="id",
        column="currency_id",
    )
    def currency_id(self, record):
        return {"currency_id": record.get("currency_id", [])[0]}


models_tree.add(SaleOrder)
