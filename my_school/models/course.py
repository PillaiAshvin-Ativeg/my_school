from odoo import models, fields

class Course(models.Model):
    _name = 'my.school.course'
    _description = 'Course'

    name = fields.Char(string='Course Name', required=True)
    description = fields.Text(string='Description')
