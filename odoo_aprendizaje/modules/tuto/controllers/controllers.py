# -*- coding: utf-8 -*-
# from odoo import http


# class Tuto(http.Controller):
#     @http.route('/tuto/tuto', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tuto/tuto/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tuto.listing', {
#             'root': '/tuto/tuto',
#             'objects': http.request.env['tuto.tuto'].search([]),
#         })

#     @http.route('/tuto/tuto/objects/<model("tuto.tuto"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tuto.object', {
#             'object': obj
#         })

