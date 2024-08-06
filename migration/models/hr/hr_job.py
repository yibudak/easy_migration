# Copyright 2024 Ahmet Yiğit Budak (https://github.com/yibudak)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from migration import models_tree
from migration.libs.migration_mapper import BaseMapper, mapping


class HrJob(BaseMapper):
    _name = "hr.job"
    _OLD_TABLE_NAME = "hr_job"
    _NEW_TABLE_NAME = "hr_job"


models_tree.add(HrJob)