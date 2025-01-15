# -*- coding: utf-8 -*-

from odoo import models, fields, api # type: ignore


class autor_modelo(models.Model):
    _name = 'gestor_biblioteca.autor_modelo'
    _description = 'gestor_biblioteca.gestor_biblioteca'

    nombre = fields.Char()
    fecha_nac = fields.Date()
    biografia = fields.Text()
    libros = fields.Text()