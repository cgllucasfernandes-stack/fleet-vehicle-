{
    #Nome do módulo na interface do Odoo
    'name': 'Reserva de Veículos da Frota',
    'version': '1.0',
    'category': 'Human Resources/Fleet',
    'summary': 'Módulo para reserva de veículos da frota por funcionários',
    #Licença padrão para módulos comunitários
    'license': 'LGPL-3',
    'author': 'Lucas Fernandes',
    'depends': [
        'fleet', 
        'hr', 
        'mail'
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/fleet_reservation_views.xml',
        'views/fleet_reservation_menu.xml', 
    ],
    'installable': True,
    'application': True,
}
