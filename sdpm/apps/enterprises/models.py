# -*- coding: utf-8 -*-
"""
    enterprises.models
    ~~~~~~~~~~~~~~

    Has the content related to models fo the enterprise.
    
    :copyright: (c) 2012 by Arruda.
"""
from django.db import models
from utils.abs_models import Abs_Named_Model

class Enterprise(Abs_Named_Model):
    "A Enterprise"
    
    class Meta:
        app_label = 'enterprises'
