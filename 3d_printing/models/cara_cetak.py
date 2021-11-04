#-*- coding: utf-8 -*-

from odoo import models, fields

class print3d(models.Model):
    _name = '3dprint.teknik'
    _description = 'daftar teknik print 3d'

    name = fields.Selection(
        string='Nama Teknik',
        selection=[('stereolithography', 'Stereolithography'), ('selective laser sintering', 'Selective Laser Sintering'), ('fused deposition modelling', 'Fused Deposition Modelling'), ('digital light processing', 'Digital Light Processing')]
    )

    harga = fields.Integer(
        string='harga_print',
        required=True
    )

    ukuran = fields.Char(
        string='ukuran design',
        required=True,
    )

    tersedia = fields.Boolean(
        string='tersedia',
        default=True
    )
    
    deskripsi = fields.Char(
        string='deskripsi',
        help='isi dengan teknik yang digunakan untuk mencetak')

    models_ids = fields.One2many(
        comodel_name = '3dprint.jeniscetakan',
        inverse_name = 'teknik_id',
        string = 'jenis cetakan'
    )

    pegawai_id = fields.Many2one(
        comodel_name = 'res.partner',
        string = 'MANAGER',
        domain = "[('is_pegawainya','=',True)]"
    )