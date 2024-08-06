# Copyright 2024 Ahmet Yiğit Budak (https://github.com/yibudak)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from migration import models_tree
from migration.libs.migration_mapper import BaseMapper, mapping


class ProjectTaskType(BaseMapper):
    _name = "project.task.type"
    _OLD_TABLE_NAME = "project_task_type"
    _NEW_TABLE_NAME = "project_task_type"


models_tree.add(ProjectTaskType)
