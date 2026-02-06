from odoo import models, fields, api, _ 
from odoo.exceptions import ValidationError

class FleetVehicleReservation(models.Model):
    _name = 'fleet.vehicle.reservation'
    _description = 'Reserva de Veículo'
    _inherit = ['mail.thread', 'mail.activity.mixin'] # Adiciona o Chatter (opcional/recomendado)
    

    # --- Campos Obrigatórios ---
    name = fields.Char(
        string='Identificador', 
        required=True, 
        copy=False, 
        readonly=True, 
        index=True, 
        default=lambda self: _('Novo')
    )
    vehicle_id = fields.Many2one('fleet.vehicle', string='Veículo', required=True, tracking=True)
    employee_id = fields.Many2one('hr.employee', string='Funcionário', required=True, tracking=True)
    start_datetime = fields.Datetime(string='Início da Reserva', required=True, tracking=True)
    end_datetime = fields.Datetime(string='Fim da Reserva', required=True, tracking=True)
    purpose = fields.Text(string='Finalidade')
    work_order_ref = fields.Char(string='Ref. Ordem de Trabalho')
    
    state = fields.Selection([
        ('draft', 'Rascunho'),
        ('confirmed', 'Confirmado'),
        ('cancel', 'Cancelado'),
    ], string='Status', default='draft', tracking=True)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            # Se o nome for 'Novo' ou estiver vazio, busca o próximo número da sequência
            if vals.get('name', _('Novo')) == _('Novo'):
                vals['name'] = self.env['ir.sequence'].next_by_code('fleet.vehicle.reservation') or _('Novo')
        return super(FleetVehicleReservation, self).create(vals_list)

    # --- Lógica de Validação (O que você aprendeu) ---
    @api.constrains('vehicle_id', 'start_datetime', 'end_datetime', 'state')
    def _check_date_overlap(self):
        for record in self:
            # A regra só se aplica se a reserva estiver confirmada
            if record.state != 'confirmed':
                continue

            # Validação básica de integridade
            if record.end_datetime <= record.start_datetime:
                raise ValidationError(_("A data de fim deve ser posterior à data de início."))

            # A Regra Matemática de Conflito: (Início A < Fim B) E (Fim A > Início B)
            domain = [
                ('id', '!=', record.id), # Não comparar a reserva com ela mesma
                ('vehicle_id', '=', record.vehicle_id.id),
                ('state', '=', 'confirmed'),
                ('start_datetime', '<', record.end_datetime),
                ('end_datetime', '>', record.start_datetime),
            ]
            
            overlap = self.search(domain, limit=1)
            if overlap:
                raise ValidationError(_(
                    "Conflito de Datas: O veículo %s já possui uma reserva confirmada "
                    "para o período de %s até %s (Referência: %s)."
                ) % (record.vehicle_id.name, overlap.start_datetime, overlap.end_datetime, overlap.name))

    # --- Ações de Botão ---
    def action_confirm(self):
        self.write({'state': 'confirmed'})

    def action_draft(self):
        self.write({'state': 'draft'})