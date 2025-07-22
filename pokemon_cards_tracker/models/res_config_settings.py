from odoo import models, fields
from odoo.exceptions import UserError


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    def action_import_pokemon_sets(self):
        sets_model = self.env['pokemon.set']
        try:
            sets_model.import_all_sets()
        except Exception as e:
            raise UserError(f"Import failed: {str(e)}")
