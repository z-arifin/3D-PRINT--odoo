#-*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ModelDasar(models.Model):
    _name = "3dprint.modeldasar"
    _description = "model dasar 3d print"
    
    ukuran = fields.Char(
        string='ukuran design',
        required=True,
    )
    
    tipe = fields.Selection(
        string='tipe material',
        selection=[('pla', 'PLA'), ('abs', 'ABS'), ('pva', 'PVA'), ('hips', 'HIPS')]
    )

class print3d(models.Model):
    _name = '3dprint.jeniscetakan'
    _description = 'daftar jenis-jenis cetakan'
    _inherit = '3dprint.modeldasar'

    name = fields.Char(
        string='jenis_cetakan',
        required=True
    )
    active = fields.Boolean(
        default=True
    )
    deskripsi = fields.Char(
        string='Deskripsi'
    )
    teknik_id = fields.Many2one(
        comodel_name='3dprint.caracetak',
        string='teknik cuci',
        required=True,
        delegate=True
    )
    deskrip = fields.Char(
        compute = '_compute_deskrip',
        string='Teknik Pencetakan'
    )
    @api.depends('teknik_id')
    def _compute_deskrip(self):
        for record in self:
            record.deskrip = record.teknik_id.deskripsicetak

    @api.onchange('tipe')
    def _onchange_field_name(self):
        if self.tipe == 'pla':
            return {
                'warning' : {
                    'title' : "Teknik Pencetakan",
                    'message' : "Rubah Teknik Pencetakan ke Golongan B"
                },
            }
        elif self.tipe == 'abs':
            return {
                'warning' : {
                    'title' : "Teknik Pencetakan",
                    'message' : "Rubah Teknik Pencetakan ke Golongan A"
                }
            }
    @api.constrains('name')
    def _check_name(self):
        for record in self:
            bahan = self.env['3dprint.jeniscetakan'].search([('name', '=', record.name), ('id', '!=', record.id)])
            if bahan:
                raise ValidationError("Material %s sudah ada" % record.name)