# -*- coding: utf-8 -*-

from django.contrib.auth import login
from django.shortcuts import redirect, get_object_or_404
from annoying.decorators import render_to

from django.contrib.auth.models import User

from enterprises.forms import RegistrationForm

from enterprises.models import Enterprise, EnterpriseMember

@render_to('user/register.html')
def register(request): 
    
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid(): 
            #Create the user
            owner_email = form.cleaned_data.get('owner_email')
            passwd = form.cleaned_data.get('password1')
            
            user = User(email=owner_email)
            user.set_password(passwd)            
            user.save()
            user.username = user.pk
            user.save()
            
            #create the enterprise
            ep_name = form.cleaned_data.get('enterprise')
            ep = Enterprise(name=ep_name)
            ep.save()
            
            #create the enterprise member
            ep_member = EnterpriseMember(user=user,enterprise=ep)
            ep_member.member_type = EnterpriseMember.MEMBER_TYPE.owner
            ep_member.save()
            
            return redirect('/')
    else:
        form = RegistrationForm()

    return locals()

