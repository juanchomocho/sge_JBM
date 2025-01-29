# -*- coding: utf-8 -*-

from odoo import models, fields, api


class modelo_socio(models.Model):
    _name = 'library_jbm.modelo_socio'
    _description = 'library_jbm.library_jbm'

    nombre = fields.Char()
    telefono = fields.Char()
    libros = fields.Many2many('library_jbm.modelo_libro', string='Libros prestados')
    