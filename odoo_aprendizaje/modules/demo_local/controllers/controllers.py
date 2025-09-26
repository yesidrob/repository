# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class GraficaController(http.Controller):

    @http.route('/grafica/datos', type='json', auth='user')
    def obtener_datos(self):
        records = request.env['mi_modulo.dato'].sudo().search([])
        return {
            'labels': [r.nombre for r in records],
            'valores': [r.valor for r in records]
        }

    @http.route('/grafica', auth='user', website=True)
    def mostrar_grafica(self, **kw):
        return request.render('demo_local.template_grafica')


