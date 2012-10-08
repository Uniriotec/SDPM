# -*- coding: utf-8 -*-
"""
    Abs_models
    ~~~~~~~~~~~~~~

    Here are some utilities models. 
    
    :copyright: (c) 2011 by Arruda.
"""

from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils import Choices
from decimal import Decimal
import datetime


class Abs_Named_Model(models.Model):    
    """
    A Class that has a name att.
    """
    
    name = models.CharField(_("Name"),blank=False, null=False, max_length=250)
    
    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name
