{
    'name': "Excel Data Importer with Charts",
    'version': '2.0.0',
    'depends': ['base', 'web'],
    'author': "Tu Nombre",
    'category': 'Tools',
    'summary': "Importar Excel y visualizar gráficos interactivos",
    'description': """
        Módulo para importar datos desde Excel y visualizarlos
        en gráficos interactivos con Plotly.js
    """,
    'data': [
        'views/templates.xml',
        'views/views.xml',
    ],
    'controllers': [
        'controllers/main.py',
    ],
    'assets': {
        'web.assets_backend': [
            'https://cdn.plot.ly/plotly-2.24.1.min.js',
            'excel_charts/static/src/js/chart_loader.js',
            'excel_charts/static/src/css/style.css',
        ],
    },
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}