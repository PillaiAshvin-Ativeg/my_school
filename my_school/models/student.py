from odoo import models, fields

class Student(models.Model):
    _name = 'my.school.student'
    _description = 'Student'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    course_id = fields.Many2one('my.school.course', string='Course')
