# -*- coding: utf-8 -*-

from odoo import models, fields, api


class modelo_producto(models.Model):
    _name = 'gestion_productos.modelo_producto'
    _description = 'gestion_productos.gestion_productos'

    nombre = fields.Char(string="Nombre del producto")
    descripcion = fields.Text(string="Descripción del producto")
    cod_producto = fields.Integer(string="Codigo del producto", required=True)
    imagen = fields.Image(string="Imagen del producto")
    categoria = fields.Selection([
        ('jardn','Jardín'),
        ('hogar', 'Hogar'),
        ('electrodomesticos', 'Electrodomésticos')
        ]
    )
    tipo_de_producto = fields.Boolean(string="Destacable")
    precio = fields.Float(string="Precio de venta")
    stock_disponible = fields.Integer(string="Stock disponible")
    fecha_de_creacion = fields.Date(default=fields.Date.today, string="Fecha de creación")
    fecha_actualizacion = fields.Date(string="Fecha de última actualización")
    activo = fields.Boolean(default=True)
    peso_del_producto = fields.Float(string="Peso del producto", digits=(10,2))
