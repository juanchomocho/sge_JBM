# -*- coding: utf-8 -*-

from odoo import models, fields, api


class modelo_libro(models.Model):
    _name = 'library_jbm.modelo_libro'
    _description = 'library_jbm.library_jbm'

    titulo = fields.Char()
    autor = fields.Many2one(comodel_name='library_jbm.modelo_autor')
    genero = fields.Selection([
        ('novela', 'Novela'),
        ('drama', 'Drama'),
        ('ciencia_ficcion', 'Ciencia ficción'),
        ('misterio', 'Misterio'),
        ('terror', 'Terror'),
        ('historico', 'Historico')
        ]
    )
    socios = fields.Many2many('library_jbm.modelo_socio')
