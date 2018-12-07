# -*- coding: utf-8 -*-
from odoo import http

# class ../user/odooDevTraning(http.Controller):
#     @http.route('/../user/odoo_dev_traning/../user/odoo_dev_traning/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/../user/odoo_dev_traning/../user/odoo_dev_traning/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('../user/odoo_dev_traning.listing', {
#             'root': '/../user/odoo_dev_traning/../user/odoo_dev_traning',
#             'objects': http.request.env['../user/odoo_dev_traning.../user/odoo_dev_traning'].search([]),
#         })

#     @http.route('/../user/odoo_dev_traning/../user/odoo_dev_traning/objects/<model("../user/odoo_dev_traning.../user/odoo_dev_traning"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('../user/odoo_dev_traning.object', {
#             'object': obj
#         })