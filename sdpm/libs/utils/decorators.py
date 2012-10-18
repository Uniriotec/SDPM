# -*- coding: utf-8 -*-
"""
    decorators
    ~~~~~~~~~~~~~~

    Here are some utilities decorators for SDPM. 
    
    :copyright: (c) 2012 by Arruda.
"""

from functools import wraps

from django.shortcuts import redirect, get_object_or_404



def enterprise_member_required(owner=False):
    
    def requirement_check(function):
        """
        Check if the user logged in is a owner of the given enterprise(enterprise_id kwarg)
        """
        from enterprises.models import Enterprise, EnterpriseMember
        @wraps(function)
        def wrapper(request, *args, **kwargs):
            enterprise_id =  kwargs.get('enterprise_id')
            enterprise = get_object_or_404(Enterprise, pk=enterprise_id)
            
            get_kwargs  = {
                           'enterprise__pk': enterprise_id,
                           'user':request.user,                           
                           }
            if owner:
                get_kwargs['member_type'] = EnterpriseMember.MEMBER_TYPE.owner
                
            member = get_object_or_404(EnterpriseMember, **get_kwargs)
                    
            return function(request, *args, **kwargs)       
        
        return wrapper
    
    return requirement_check
