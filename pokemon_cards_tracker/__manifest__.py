{
    'name': 'Pokemon Cards Tracker',
    'version': '18.0.1.0.1',
    'summary': 'Module to manage and track Pokémon card collection',
    'description': 'Provides a structure to manage and track Pokémon card details in Odoo.',
    'author': 'Your Name or Company',
    'website': 'https://yourwebsite.com',
    'category': 'Tools',
    'depends': ['base'],
    'external_dependencies': {
        'python': ['pokemontcgsdk'],
    },
    'data': [
        'views/pokemon_views.xml',
        'views/res_config_settings.xml',
        'security/ir.model.access.csv',

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
