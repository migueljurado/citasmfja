# -*- coding: utf-8 -*-
from odoo import http

# class Citasmja(http.Controller):
#     @http.route('/citasmja/citasmja/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/citasmja/citasmja/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('citasmja.listing', {
#             'root': '/citasmja/citasmja',
#             'objects': http.request.env['citasmja.citasmja'].search([]),
#         })

#     @http.route('/citasmja/citasmja/objects/<model("citasmja.citasmja"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('citasmja.object', {
#             'object': obj
#         })