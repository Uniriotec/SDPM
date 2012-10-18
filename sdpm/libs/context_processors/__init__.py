# -*- coding: utf-8 -*-

    
def add_logged_member(request):
    " adds 'logged_member'(enterprise member) if there is one "
    from enterprises.models import Enterprise, EnterpriseMember
    
    user = request.user    
    if user== None or not user.is_authenticated():
        return {}
    
    logged_member = None
    try:
        logged_member = user.enterprisemember_set.get()
    except EnterpriseMember.DoesNotExist:
        pass
    
    
    return {'logged_member':logged_member, }


