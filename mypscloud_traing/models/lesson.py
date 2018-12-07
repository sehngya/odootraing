# -*- coding: utf-8 -*-

from odoo import api, fields, models

class TrainingLesson(models.Model):
    _name = 'mypscloud.traing.lesson'
    _rec_name = 'name'
    
    name = fields.Char(u'课程名称',size=64,default=u'课程名称',transtrate=True)
    teacher_id = fields.Char(u'教师',size=64)
    start_date = fields.Date(string='开始时间')
    end_date = fields.Date(string='结束时间')
    continue_days = fields.Integer(string='持续天数', compute='_compute_days', store=True)
   # subject_id = fields.Many2one('mypscloud.traing.subject', string='科目')
    seat_qty = fields.Char(u'测试')
    #person_id = fields.Many2one('res.partner', related='subject_id.person_id', readonly=True)
    desc = fields.Text(string='描述')
