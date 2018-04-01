# -*- coding: utf-8 -*-
 
from odoo import models, fields, api, _

class citasmja(models.Model):
	_name = 'citasmja.start'
	orden = fields.Char()
	autor = fields.Char()
	cita = fields.Char()
	fecha = fields.Char()