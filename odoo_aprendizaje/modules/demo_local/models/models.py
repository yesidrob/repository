# -*- coding: utf-8 -*-

from odoo import models, fields

class Datos(models.Model):
    _name = 'mi_modulo.dato'
    _description = 'Datos para Gráfica'

    nombre = fields.Char(string='Nombre')
    valor = fields.Integer(string='Valor')


