# -*- coding: utf-8 -*-
"""
    accounts.models
    ~~~~~~~~~~~~~~

    Has the content related to the account of the enterprise.
    
    :copyright: (c) 2012 by Arruda.
"""
from django.db import models
from model_utils import Choices
#from django.contrib.auth.models import User

class Member(models.Model):
    """
    """
    MEMBER_TYPE = Choices(
                            (0, 'member', 'Member'),
                            (1, 'owner', 'Owner'),
                            )
    user = models.ForeignKey('auth.User', related_name="members")
    member_type = models.IntegerField(choices=MEMBER_TYPE, default=MEMBER_TYPE.member)
    
    class Meta:
        app_label = 'accounts'

    def __unicode__(self):
        return "%s" % str(self.user.username)
        
