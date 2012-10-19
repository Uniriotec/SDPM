# -*- coding: utf-8 -*-

from django.contrib.auth import login
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from annoying.decorators import render_to

from django.contrib.auth.models import User

from utils.decorators import enterprise_member_required

from enterprises.forms import RegistrationForm, NewEnterpriseMemberForm

from enterprises.models import Enterprise, EnterpriseMember

@render_to('users/register.html')
def register(request): 
    if request.user != None and request.user.is_authenticated():
        return redirect('/')
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
            user.backend='user_backends.email_username.EmailOrUsernameModelBackend'
            
            #create the enterprise
            ep_name = form.cleaned_data.get('enterprise')
            ep = Enterprise(name=ep_name)
            ep.save()
            
            #create the enterprise member
            ep_member = EnterpriseMember(user=user,enterprise=ep)
            ep_member.member_type = EnterpriseMember.MEMBER_TYPE.owner
            ep_member.save()
            
            #logs the new user
            login(request,user)
            return redirect('/')
    else:
        form = RegistrationForm()

    return locals()

@login_required
@enterprise_member_required(owner=True)
@render_to('enterprises/add_member.html')
def add_member(request):
    """
    Add a new member to a given enterprise
    """
    enterprise = Enterprise.get_from_user_or_404(request.user)
    
    if request.method == 'POST':
        form = NewEnterpriseMemberForm(request.POST)
        if form.is_valid(): 
            
            #Create the user
            owner_email = form.cleaned_data.get('member_email')
            passwd = form.cleaned_data.get('password1')
            
            user = User(email=owner_email)
            user.set_password(passwd)            
            user.save()
            user.username = user.pk 
            user.backend='user_backends.email_username.EmailOrUsernameModelBackend'
            user.save()
            
            
            #create the enterprise member
            ep_member = form.save(commit=False)#(user=user,enterprise=ep)
            ep_member.user = user
            ep_member.enterprise = enterprise
            ep_member.save()
            
            return redirect('/')
    else:
        form = NewEnterpriseMemberForm()

    return locals()


@login_required
@enterprise_member_required()
@render_to('enterprises/members_list.html')
def manage_members(request):
    """
    Show other options to manage the enterprise, like:
    Add members and change their type
    """
   
    enterprise = Enterprise.get_from_user_or_404(request.user)
    return locals()