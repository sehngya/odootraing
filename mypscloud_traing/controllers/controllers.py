# -*- coding: utf-8 -*-
from odoo import http

# class ../user/mypscloudTraing(http.Controller):
#     @http.route('/../user/mypscloud_traing/../user/mypscloud_traing/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/../user/mypscloud_traing/../user/mypscloud_traing/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('../user/mypscloud_traing.listing', {
#             'root': '/../user/mypscloud_traing/../user/mypscloud_traing',
#             'objects': http.request.env['../user/mypscloud_traing.../user/mypscloud_traing'].search([]),
#         })

#     @http.route('/../user/mypscloud_traing/../user/mypscloud_traing/objects/<model("../user/mypscloud_traing.../user/mypscloud_traing"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('../user/mypscloud_traing.object', {
#             'object': obj
#         })