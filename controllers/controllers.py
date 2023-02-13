# -*- coding: utf-8 -*-
# from odoo import http


# class IndexDaysCount(http.Controller):
#     @http.route('/index_days_count/index_days_count/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/index_days_count/index_days_count/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('index_days_count.listing', {
#             'root': '/index_days_count/index_days_count',
#             'objects': http.request.env['index_days_count.index_days_count'].search([]),
#         })

#     @http.route('/index_days_count/index_days_count/objects/<model("index_days_count.index_days_count"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('index_days_count.object', {
#             'object': obj
#         })
