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
        #'data/sequence.xml', houve algum erro na qual eu não sei identificar, por isso não consigo utlizar o 'sequence.xml' aqui
        'views/fleet_reservation_views.xml',
        #'views/fleet_reservation_menus.xml', Aconteceu o mesmo caso aqui, mas eu deixei os codigos deles no diretório caso queira 
    ],
    'installable': True,
    'application': True,
}
