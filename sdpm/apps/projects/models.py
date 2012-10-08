# -*- coding: utf-8 -*-
"""
    projects.models
    ~~~~~~~~~~~~~~

    Has the content related to models for projects.
    
    :copyright: (c) 2012 by Arruda.
"""
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
    
    enterprise = models.ForeignKey('enterprises.Enterprise')  
    members = models.ManyToManyField('enterprises.EnterpriseMember', related_name="projects", through='ProjectMember') 
       
    points = models.PositiveIntegerField(_("Points"),default=0)
    
    class Meta:
        app_label = 'projects'
    

class ProjectMember(models.Model):
    "A member of a given Project"
    
    member = models.ForeignKey('enterprises.EnterpriseMember')    
    project = models.ForeignKey(Project)
    
    class Meta:
        app_label = 'projects'
    
    def __unicode__(self):
        return "% (% - %) " % (self.member.user.username, self.enterprise.name, self.member_type) 
    
    
    
class Task(Abs_Named_Model):
    """Represent a task in a given project
    """
    STATUS = Choices(
                        ('n', 'new', _('New')),
                        ('dg', 'doing', _('Doing')),
                        ('d', 'done', _('Done')),
                    )
    
    status = models.CharField(_('Status'), choices=STATUS, default=STATUS.new, max_length=2)
    
    class Meta:
        app_label = 'projects'
    