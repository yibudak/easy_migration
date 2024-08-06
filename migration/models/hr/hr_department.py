# Copyright 2024 Ahmet Yiğit Budak (https://github.com/yibudak)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from migration import models_tree
from migration.libs.migration_mapper import BaseMapper, mapping


class HrDepartment(BaseMapper):
    _name = "hr.department"
    _OLD_TABLE_NAME = "hr_department"
    _NEW_TABLE_NAME = "hr_department"


models_tree.add(HrDepartment)
