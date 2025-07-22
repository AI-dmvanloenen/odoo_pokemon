from odoo import models, fields


class PokemonCard(models.Model):
    _name = 'pokemon.card'
    _description = 'Pokemon Card'
    _rec_name = 'display_name'

    # Identification
    card_id = fields.Char(string='Card ID', required=True,
                          index=True, unique=True)
    name = fields.Char(string='Name', required=True)
    display_name = fields.Char(
        string='Display Name', compute='_compute_display_name')
    set_id = fields.Many2one(
        'pokemon.set', string='Set', required=True, index=True)
    artist_id = fields.Many2one('pokemon.artist', string='Artist', index=True)

    # Stats & Details
    hp = fields.Integer(string='HP')
    evolves_from = fields.Char(string='Evolves From')
    regulation_mark = fields.Char(string='Regulation Mark')
    flavor_text = fields.Text(string='Flavor Text')
    number = fields.Char(string='Card Number')
    rarity = fields.Char(string='Rarity')
    artist = fields.Char(string='Artist')
    converted_retreat_cost = fields.Integer(string='Converted Retreat Cost')

    # Lists
    # abilities = fields.Json(string='Abilities')
    # ancient_trait = fields.Json(string='Ancient Trait')
    # attacks = fields.Json(string='Attacks')
    # resistances = fields.Json(string='Resistances')
    # retreat_cost = fields.Json(string='Retreat Cost')
    # rules = fields.Json(string='Rules')
    # subtypes = fields.Json(string='Subtypes')
    # types = fields.Json(string='Types')
    # weaknesses = fields.Json(string='Weaknesses')
    # national_pokedex_numbers = fields.Json(string='National Pokedex Numbers')

    # Complex nested objects
    # images = fields.Json(string='Images')
    # legalities = fields.Json(string='Legalities')
    # set_info = fields.Json(string='Set')
    # tcgplayer_info = fields.Json(string='TCG Player Info')

    # supertype = fields.Char(string='Supertype')

    _sql_constraints = [
        ('card_id_unique', 'unique(card_id)', 'The Card ID must be unique.'),
    ]

    def _compute_display_name(self):
        for rec in self:
            rec.display_name = f"{rec.name or 'Unknown'} ({rec.number or '-'})"
