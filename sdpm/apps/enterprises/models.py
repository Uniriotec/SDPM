# -*- coding: utf-8 -*-
"""
    enterprises.models
    ~~~~~~~~~~~~~~

    Has the content related to models fo the enterprise.
    
    :copyright: (c) 2012 by Arruda.
"""
from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils import Choices

from utils.abs_models import Abs_Named_Model

class Enterprise(Abs_Named_Model):
    "A Enterprise"
    
    class Meta:
        app_label = 'enterprises'



class EnterpriseMember(models.Model):
    "A member from a given Enterprise"
    MEMBER_TYPE = Choices(
                            (0, 'owner', _('Owner')),
                            (1, 'member', _('Member')),
                            )
    
    user = models.ForeignKey('auth.User')    
    enterprise = models.ForeignKey(Enterprise, related_name='members')
    
    member_type = models.IntegerField(_("Member Type"),choices=MEMBER_TYPE, default=MEMBER_TYPE.member)
    
    class Meta:
        app_label = 'enterprises'

    def __unicode__(self):
        return "%s (%s - %s) " % (self.user.email, self.enterprise.name, self.MEMBER_TYPE[self.member_type][1]) 
    
    