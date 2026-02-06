{
    'name': 'Reserva de Veículos da Frota',
    'version': '1.0',
    'category': 'Human Resources/Fleet',
    'summary': 'Módulo para reserva de veículos da frota por funcionários',
    'license': 'LGPL-3',
    'author': 'Seu Nome',
    'depends': [
        'fleet', 
        'hr', 
        'mail'
    ],
    'data': [
        'security/ir.model.access.csv',
        #'data/sequence.xml',
        #'views/fleet_reservation_views.xml',
        #'views/fleet_reservation_menus.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}