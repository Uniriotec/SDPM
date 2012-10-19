# -*- coding: utf-8 -*-

from django.contrib.auth import login
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from annoying.decorators import render_to

from django.forms.models import inlineformset_factory

from django.contrib.auth.models import User

from utils.decorators import enterprise_member_required

from enterprises.models import Enterprise, EnterpriseMember

from projects.forms import NewProjectForm, NewProjectMemberForm
from projects.models import Project, ProjectMember

@login_required
@enterprise_member_required(owner=True)
@render_to('projects/add_project.html')
def add_project(request):
    """
    Add a new project to a given enterprise
    """
    
    
    enterprise = Enterprise.get_from_user_or_404(request.user)
    
    if request.method == 'POST':
        form = NewProjectForm(request.POST)
        if form.is_valid(): 
            new_project = form.save(commit=False)
            new_project.enterprise = enterprise
            
            new_project.save()     
            
            return redirect('/')
    else:
        form = NewProjectForm()


    return locals()
