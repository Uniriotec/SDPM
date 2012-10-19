# -*- coding: utf-8 -*-
"""
    projects.models
    ~~~~~~~~~~~~~~

    Has the content related to models for projects.
    
    :copyright: (c) 2012 by Arruda.
"""
import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils import Choices

from utils.abs_models import Abs_Named_Model

    
    
class Project(Abs_Named_Model):
    """
    A Project from a enterprise
    It has members, points , tasks and transactions.
    
    --
    spend_points: How many points have been spent already
    
    """
    
    enterprise = models.ForeignKey('enterprises.Enterprise',related_name='projects')  
    members = models.ManyToManyField('enterprises.EnterpriseMember', related_name="projects")#, through='ProjectMember') 
       
    points = models.PositiveIntegerField(_("Points"),default=0)
    
    class Meta:
        app_label = 'projects'
    

#class ProjectMember(models.Model):
#    "A member of a given Project"
#    
#    member = models.ForeignKey('enterprises.EnterpriseMember')    
#    project = models.ForeignKey(Project)
#    
#    class Meta:
#        app_label = 'projects'
#    
#    def __unicode__(self):
#        return "%s (%s - %s) " % (self.member.user.username, self.project.enterprise.name, self.member.MEMBER_TYPE[self.member.member_type][1]) 
    
    
    
class Task(Abs_Named_Model):
    """Represent a task in a given project
    """
    STATUS = Choices(
                        ('n', 'new', _('New')),
                        ('dg', 'doing', _('Doing')),
                        ('d', 'done', _('Done')),
                    )
    description = models.TextField(_('Description'), null=True,blank=True)
    status = models.CharField(_('Status'), choices=STATUS, default=STATUS.new, max_length=2)
    
    project = models.ForeignKey(Project,related_name='tasks')
    
    points = models.PositiveIntegerField(_("Points"),default=0)
    
    assigned = models.ForeignKey('enterprises.EnterpriseMember',null=True,blank=True, related_name='tasks')
    
    start_date = models.DateField(_("Starting Date"), default=datetime.date.today, null=True, blank=True)
    end_date = models.DateField(_("Ending Date"), default=datetime.date.today, null=True, blank=True)
    
    class Meta:
        app_label = 'projects'
        