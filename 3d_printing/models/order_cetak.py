from odoo import api, fields, models


class OrderCuci(models.Model):
    _name = '3dprint.order'
    _description = 'Daftar Order Cetak 3s Printing'

    name = fields.Many2one(
        comodel_name='res.partner', 
        string='Customer',
        domain="[('is_customernya','=',True)]",
        delegate=True)  
    
    tanggal_masuk = fields.Datetime(
        default=fields.Datetime.now,
        )
    
    detailcucian_ids = fields.One2many(
        comodel_name='3dprint.detailcetakan', 
        inverse_name='order_id', 
        string='Detail Order')
    
    jml_pesanan = fields.Char(
        compute='_compute_jml_pesanan', 
        string='Jumlah Pesanan')
    
    @api.depends('detailcucian_ids')
    def _compute_jml_pesanan(self):        
        for record in self:
            record.jml_pesanan +=len(record.detailcetakan_ids)
            
    total_harga = fields.Integer(compute='_compute_total_harga', string='Total Tagihan')
   
    @api.model
    def _compute_total_harga(self):        
        for record in self:           
                total = sum(self.env['3dprint.detailcetakan'].search([('order_id','=', record.id)]).mapped('jumlah_harga'))
                record.total_harga = total
            

            
            
class DetailCucian(models.Model):
    _name = '3dprint.detailcetakan'
    _description = 'Detail Cetakan 3d Print'
    
    name = fields.Char(string='Kode Order')    
    
    order_id = fields.Many2one(
        comodel_name='3dprint.order', 
        string='Kode Order')
         
    jenis = fields.Many2one(
        comodel_name='3dprint.jeniscetakan',
        string='Bahan Cetakan')
    
    harga = fields.Integer(
        compute='_compute_harga', 
        string='Harga per Kg')
    
    @api.depends('jenis')
    def _compute_harga(self):
        for record in self:
            record.harga = record.jenis.harga
        
    jumlah_harga = fields.Integer(
        compute='_compute_field_name', 
        string='Jumlah Harga')
    
    @api.depends('berat')
    def _compute_field_name(self):
        for record in self:
            record.jumlah_harga = record.berat * record.harga