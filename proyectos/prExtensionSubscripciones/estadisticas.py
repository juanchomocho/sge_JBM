# -*- coding: utf-8 -*-

from odoo import models, fields, api


class estadisticas(models.Model):
    _name = 'subscription.estadisticas'
    _description = 'subscription.subscription'
    _sql_constraints = [
        ('unique_name', 'unique(name)', "El nombre debe ser único"),
    ]

    fecha_registro = fields.Date(string="fecha")
    numero_subscripcion = fields.Integer(string="Numero de subscripciones activas")
    ingresos_generados = fields.Float()
    tasa_renovacion = fields.Float(compute="_renovation_rate_calculation")
    tasa_cancelacion = fields.Float(compute="_cancelation_rate_calculation")
    numero_renovaciones = fields.Integer()
    nuevas_suscripciones = fields.Integer()
    suscripciones_canceladas = fields.Integer()
    clientes_nuevos = fields.Integer(string="nuevos clientes")
    clientes_recurrentes = fields.Integer(string="Clientes recurrentes")
    ingresos_promedios_por_usuarios = fields.Float(compute="_ipu_calculation")
    tasa_conversion = fields.Float()
    tasa_perdida_clientes = fields.Float(compute="_cancelation_rate2_calculation")
    valor_vida_cliente = fields.Float()
    costo_adquisicion_cliente = fields.Float()
    notas = fields.Text()
    relacion_suscripciones = fields.One2many(comodel_name='subscription.subs', inverse_name='subscription_code')


    @api.depends('numero_renovaciones', 'numero_subscripcion')
    def _renovation_rate_calculation(self):
        for subs in self:
            if subs.numero_renovaciones != 0 and subs.numero_subscripcion != 0:
                subs.tasa_renovacion = (subs.numero_renovaciones / subs.numero_subscripcion) * 100
            else:
                subs.tasa_renovacion = 0

    @api.depends('suscripciones_canceladas', 'numero_subscripcion')
    def _cancelation_rate_calculation(self):
        for subs in self:
            if subs.suscripciones_canceladas != 0 and subs.numero_subscripcion != 0:
                subs.tasa_cancelacion = (subs.suscripciones_canceladas / subs.numero_subscripcion) * 100
            else:
                subs.tasa_cancelacion = 0

    @api.depends('suscripciones_canceladas', 'numero_subscripcion')
    def _cancelation_rate2_calculation(self):
        for subs in self:
            if subs.suscripciones_canceladas != 0 and subs.numero_subscripcion != 0:
                subs.tasa_perdida_clientes = (subs.suscripciones_canceladas / subs.numero_subscripcion) * 100
            else:
                subs.tasa_perdida_clientes = 0

    @api.depends('valor_vida_cliente', 'numero_subscripcion')
    def _ipu_calculation(self):
        for subs in self:
            if subs.valor_vida_cliente != 0 and subs.numero_subscripcion != 0:
                subs.ingresos_promedios_por_usuarios = (subs.valor_vida_cliente / subs.numero_subscripcion) * 100
            else:
                subs.ingresos_promedios_por_usuarios = 0