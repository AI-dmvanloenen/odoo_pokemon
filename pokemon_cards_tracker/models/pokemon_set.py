from odoo import models, fields, api

import base64
import requests
from datetime import datetime
from pokemontcgsdk import Set


class PokemonSet(models.Model):
    _name = 'pokemon.set'
    _description = 'Pokemon Set'
    _rec_name = 'name'

    set_id = fields.Char(string='Set ID', required=True, index=True, unique=True, readonly=True)
    name = fields.Char(string='Name', required=True, readonly=True)
    printed_total = fields.Integer(string='Printed Total', readonly=True)
    total = fields.Integer(string='Total Cards', readonly=True)
    ptcgo_code = fields.Char(string='PTCGO Code', readonly=True)
    release_date = fields.Date(string='Release Date', readonly=True)
    updated_at = fields.Datetime(string='Updated At', readonly=True)
    series = fields.Char(string='Series', readonly=True)
    priority = fields.Selection([('0', 'Low'), ('1', 'High')], string='Priority', default='0',)

    # Todo delete this field when the legalities are implemented
    images = fields.Json(string='Images', readonly=True)
    favorite = fields.Boolean(string='Favourite', default=False)

    image_symbol_url = fields.Char("Image: Symbol URL")
    image_logo_url = fields.Char("Image: Logo URL")

    legalities = fields.Json(string='Legalities', readonly=True)

    _sql_constraints = [
        ('set_id_unique', 'unique(set_id)', 'The Set ID must be unique.'),
    ]

    def import_all_sets(self):
        existing_ids = set(self.env['pokemon.set'].search([]).mapped('set_id'))
        sets = Set.all()
        new_vals = []

        for s in sets:
            if s.id in existing_ids:
                continue

            release_date = datetime.strptime(s.releaseDate, '%Y/%m/%d').strftime('%Y-%m-%d')
            symbol_img = base64.b64encode(requests.get(s.images.symbol).content)
            logo_img = base64.b64encode(requests.get(s.images.logo).content)

            new_vals.append({
                'set_id': s.id,
                'name': s.name,
                'printed_total': s.printedTotal,
                'total': s.total,
                'ptcgo_code': s.ptcgoCode,
                'release_date': release_date,
                'series': s.series,
                'image_symbol_url': symbol_img,
                'image_logo_url': logo_img,
                # 'images': s.images,
                # 'legalities': s.legalities,
            })

        if new_vals:
            self.env['pokemon.set'].with_context(allow_write_readonly_fields=True).create(new_vals)

        @api.model
        def create(self, vals):
            if self.env.context.get('allow_write_readonly_fields'):
                self = self.with_context({'bypass_readonly': True})
            return super().create(vals)

        def write(self, vals):
            if self.env.context.get('allow_write_readonly_fields'):
                self = self.with_context({'bypass_readonly': True})
            return super().write(vals)
