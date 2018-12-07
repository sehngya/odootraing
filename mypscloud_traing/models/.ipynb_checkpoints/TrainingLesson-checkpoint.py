# -*- coding: utf-8 -*-

from odoo import api, fields, models

class TrainingLesson(Modes.model):
    _name = 'traing.lesson'
    _rec_name = 'name'
    
    name = fields.Char(u'课程名称'，size=64,default=u'课程名称',transtrate=True)
    teacher_id = Many2one('traing.teacher',u'教师')
    start_date = fields.Date(string='开始时间')
    end_date = fields.Date(string='结束时间')
    desc = fields.Text(string='描述')
    lesson_ids = 