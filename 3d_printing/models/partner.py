from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Partner(models.Model):
    _inherit = 'res.partner'

    is_pegawainya = fields.Boolean(
        string='Pegawai', 
        default=False
        )
    is_customernya = fields.Boolean(
        string='Customer', 
        default=False
        )
    Order_ids = fields.One2many(
        comodel_name='3dprint.order', 
        inverse_name='name', 
        string='Nama Order')