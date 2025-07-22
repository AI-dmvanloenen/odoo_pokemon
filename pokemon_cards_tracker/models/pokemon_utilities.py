from odoo import models, fields


class PokemonArtist(models.Model):
    _name = 'pokemon.artist'
    _description = 'Artist='
    name = fields.Char(string='Name', required=True, index=True)


# class PokemonType(models.Model):
#     _name = 'pokemon.type'
#     _description = 'Pokemon Type'
#     name = fields.Char(string='Type', required=True, index=True)


# class PokemonSupertype(models.Model):
#     _name = 'pokemon.supertype'
#     _description = 'Pokemon Supertype'
#     name = fields.Char(string='Supertype', required=True, index=True)


# class PokemonSubtype(models.Model):
#     _name = 'pokemon.subtype'
#     _description = 'Pokemon Subtype'
#     name = fields.Char(string='Subtype', required=True, index=True)


# class PokemonRarity(models.Model):
#     _name = 'pokemon.rarity'
#     _description = 'Pokemon Rarity'
#     name = fields.Char(string='Rarity', required=True, index=True)


# class PokemonClassCard(models.Model):
#     _name = 'pokemon.class_card'
#     _description = 'Pokemon Class Card'
#     name = fields.Char(string='Card Class', required=True, index=True)


# class PokemonClassSet(models.Model):
#     _name = 'pokemon.class_set'
#     _description = 'Pokemon Class Set'
#     name = fields.Char(string='Set Class', required=True, index=True)
