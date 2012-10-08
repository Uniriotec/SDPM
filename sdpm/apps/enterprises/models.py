# -*- coding: utf-8 -*-
"""
    enterprises.models
    ~~~~~~~~~~~~~~

    Has the content related to models fo the enterprise.
    
    :copyright: (c) 2012 by Arruda.
"""
from django.db import models
from model_utils import Choices

from utils.abs_models import Abs_Named_Model

class Enterprise(Abs_Named_Model):
    "A Enterprise"
    
    class Meta:
        app_label = 'enterprises'



class EnterpriseMember(models.Model):
    "A member from a given Enterprise"
    MEMBER_TYPE = Choices(
                            (0, 'owner', 'Owner'),
                            (1, 'member', 'Member'),
                            )
    
    user = models.ForeignKey('auth.User')    
    enterprise = models.ForeignKey(Enterprise, related_name='members')
    
    member_type = models.IntegerField(choices=MEMBER_TYPE, default=MEMBER_TYPE.member)
    
    def __unicode__(self):
        return "% (% - %) " % (self.user.username, self.enterprise.name, self.member_type) 
    
    