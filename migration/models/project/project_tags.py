# Copyright 2024 Ahmet Yiğit Budak (https://github.com/yibudak)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from migration import models_tree
from migration.libs.migration_mapper import BaseMapper, mapping


class ProjectTags(BaseMapper):
    _name = "project.tags"
    _OLD_TABLE_NAME = "project_tags"
    _NEW_TABLE_NAME = "project_tags"


models_tree.add(ProjectTags)