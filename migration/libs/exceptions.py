# Copyright 2024 Ahmet Yiğit Budak (https://github.com/yibudak)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
class MissingFieldError(Exception):

    def __init__(self, model, fields):
        self.fields = fields
        self.model = model
        self.message = (
            "The following fields are missing in the model."
            " Please write mapping functions for them.\n%s: %s"
            % (model, fields)
        )
        super().__init__(self.message)
