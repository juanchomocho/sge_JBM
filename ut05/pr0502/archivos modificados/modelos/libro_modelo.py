# -*- coding: utf-8 -*-

from odoo import models, fields, api


class libro_modelo(models.Model):
    _name = 'gestor_biblioteca.libro_modelo'
    _description = 'gestor_biblioteca.gestor_biblioteca'

    nombre = fields.Char()
    autor = fields.Char()
    fecha_publicacion = fields.Date()
    IBSN = fields.Integer()
    sinopsis = fields.Text()