# -*- coding: utf-8 -*-
"""
    projects.models
    ~~~~~~~~~~~~~~

    Has the content related to models for projects.
    
    :copyright: (c) 2012 by Arruda.
"""
from django.db import models
from model_utils import Choices

from utils.abs_models import Abs_Named_Model

    
    
class Project(Abs_Named_Model):
    "A Project from a enterprise"
    enterprise = models.ForeignKey('enterprises.Enterprise')  
    members = models.ManyToManyField('enterprises.EnterpriseMember', related_name="projects", through='ProjectMember')    
    

class ProjectMember(models.Model):
    "A member of a given Project"
    
    member = models.ForeignKey('enterprises.EnterpriseMember')    
    project = models.ForeignKey(Project)
    
    
    def __unicode__(self):
        return "% (% - %) " % (self.member.user.username, self.enterprise.name, self.member_type) 