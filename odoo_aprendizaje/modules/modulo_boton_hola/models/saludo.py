from odoo import models, fields

class Saludo(models.Model):
    _name = 'modulo_boton_hola.saludo'
    _description = 'Modelo de saludo'

    nombre = fields.Char(string='Nombre')

    def accion_imprimir_hola(self):
        print("Hola desde el botón 🖐️")
