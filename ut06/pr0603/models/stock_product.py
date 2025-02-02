# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import  ValidationError


class stock_product(models.Model):
    _name = 'stock_management.stock_product'
    _description = 'stock_management.stock_product'
    _sql_constraints = [
        ('unique_name', 'unique(name)', "El nombre debe ser único"),
        ('check_stock', 'CHECK(stock > 0)', 'El stock debe ser mayor de 0')
    ]


    name = fields.Char()
    category = fields.Selection([
        ('microprocesadores', 'Microprocesadores'),
        ('graficas', 'Graficas'),
        ('moviles', 'Moviles')
    ])
    price = fields.Float()
    quantity = fields.Integer()
    total_value = fields.Float()
    minimum_quantity = fields.Integer()
    stock_status = fields.Selection([
        ('normal_status', 'normal'),
        ('low_status', 'Low Stock')
    ],compute="_status_calculation")
    full_name = fields.Char(compute="_name_calculation")


    @api.constrains('price')
    def _price_restriccion(self):
        for record in self:
            if record.price <= 0:
                raise ValidationError('El precio debe ser mayor de 0')
    
    @api.constrains('quantity')
    def _quantity_restriccion(self):
        for record in self:
            if record.quantity < 0:
                raise ValidationError('La cantidad debe ser mayor a 0')
            
    @api.constrains('total_value')
    def _total_restriccion(self):
        for record in self:
            if record.total_value > 100000:
                raise ValidationError('El valor total no puede ser mayor de 100000')
            
    @api.constrains('category')
    def _category_restriccion(self):
        for record in self:
            if not record.category:
                raise ValidationError('La categoría no puede estar vacia')

    @api.depends('quantity', 'minimum_quantity')
    def _status_calculation(self):
        for product in self:
            if product.quantity < product.minimum_quantity:
                product.stock_status = 'low_status'
            else:
                product.stock_status = 'normal_status'

    @api.depends('name', 'category')
    def _name_calculation(self):
        for product in self:
            nombre = product.name or ''
            categoria = product.category or ''
            product.full_name = nombre + '(' + categoria + ')'
