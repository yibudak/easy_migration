# Copyright 2024 Ahmet Yiğit Budak (https://github.com/yibudak)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from migration import models_tree
from migration.libs.migration_mapper import BaseMapper, mapping


class ProjectTask(BaseMapper):
    _name = "project.task"
    _OLD_TABLE_NAME = "project_task"
    _NEW_TABLE_NAME = "project_task"


models_tree.add(ProjectTask)