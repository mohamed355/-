-*- coding: utf-8 -*-

 from odoo import models, fields, api


class hospital(models.Model):
    _name = 'hospital.Hope'
    _description = 'Hope hospital'

    name = fields.Char(string='title' , reqoinrd=true ,help= "ادخل بيانات المريض"
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
