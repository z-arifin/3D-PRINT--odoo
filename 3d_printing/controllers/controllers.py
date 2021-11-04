from odoo import http, models, fields
from odoo.http import request
import json


class Wikulaundry(http.Controller):
    @http.route('/bahancetak', auth='public')
    def get_models(self, **kwargs):
        order = request.env['3dprint.jeniscetakan'].search([])
        value = []
        for ord in order:
            value.append({
                'nama' : ord.name,
                'ukuran' : ord.ukuran,
                'tipe' : ord.tipe
            })
        return json.dumps(value)

    @http.route('/caracetak', auth='public')
    def get_caracuci(self, **kwargs):
        caracetak = request.env['3dprint.caracetak'].search([])
        value = []
        for cc in caracetak:
            value.append({
                'nama' : cc.name,
                'tingkat_ukuran' : cc.ukuran,
                'harga_per_kg' : cc.harga
            })
        return json.dumps(value)