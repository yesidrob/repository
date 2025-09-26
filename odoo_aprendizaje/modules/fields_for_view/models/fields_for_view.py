from odoo import models, fields

class FieldsForView(models.Model):
    _name = 'fields.for.view'
    _description = 'Fields for View'

    name = fields.Char(string="Field Name", required=True)
    type = fields.Selection(
        selection=[
            ('char', 'Char'),
            ('text', 'Text'),
            ('integer', 'Integer'),
            ('float', 'Float'),
            ('boolean', 'Boolean'),
            ('many2one', 'Many2one'),
            ('one2many', 'One2many'),
            ('many2many', 'Many2many'),
        ],
        string="Field Type",
        required=True
    )
    view = fields.Char(string="View XML ID", required=True)
    model = fields.Char(string="Model Technical Name", required=True)


