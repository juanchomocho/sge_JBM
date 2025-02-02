# -*- coding: utf-8 -*-

from odoo import models, fields, api


class subs(models.Model):
    _name = 'subscription.subs'
    _description = 'subscription.subscription'
    _sql_constraints = [
        ('unique_name', 'unique(name)', "El nombre debe ser único"),
    ]

    name = fields.Char(required=True)
    customer_id = fields.Many2one(required=True, comodel_name='res.partner')
    subscription_code = fields.Char(required=True)
    start_date = fields.Date(required=True)
    end_date = fields.Date()
    duration_months = fields.Integer()
    renewal_date = fields.Date()
    status = fields.Selection([
        ('active', 'Active'),
        ('expired', 'Expired'),
        ('pending', 'Pending'),
        ('cancelled', 'Cancelled')
    ])
    is_renewable = fields.Boolean()
    auto_renewal = fields.Boolean()
    price = fields.Float()
    usage_limit = fields.Integer()
    current_usage = fields.Integer()
    use_percent = fields.Float(compute='_percent_calculation')

    def boton(self):
        self.duration_months=self.duration_months + 15

    @api.depends('usage_limit', 'current_usage')
    def _percent_calculation(self):
        for record in self:
            if record.usage_limit:
                record.use_percent = (record.current_usage / record.usage_limit) * 100
            else:
                record.use_percent = 0