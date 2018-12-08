# -*- coding: utf-8 -*-

from odoo import api, fields, models

class TrainingSubject(models.Model):
    _name = 'mypscloud.traing.subject'
    _rec_name = 'name'
    _description = '科目表单'
    
    
    name = fields.Char(u'科目名称',size=64,default=u'科目名称',translate=True)
    preson = fields.Char(u'负责人',size=64,default=u'科目负责人',trantrate=True)
    #'person_id' = fields.Many2one('res.partner', u'负责人')
    desc = fields.Text(string='描述')
    lesson_ids = fields.One2many('mypscloud.traing.lesson','lesson_id','课程列表')
    #lesson_ids = fields.Char(u'课程',size=64)
    
    