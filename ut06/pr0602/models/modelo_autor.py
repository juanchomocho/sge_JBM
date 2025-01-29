# -*- coding: utf-8 -*-

from odoo import models, fields, api


class modelo_autor(models.Model):
    _name = 'library_jbm.modelo_autor'
    _description = 'library_jbm.library_jbm'

    name = fields.Char(string='nombre')
    pais_origen = fields.Many2one(comodel_name='res.country', string='Pais de origen')
    libros = fields.One2many(comodel_name='library_jbm.modelo_libro', inverse_name='titulo')
