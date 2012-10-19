# -*- coding: utf-8 -*-

from django.contrib.auth import login
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from annoying.decorators import render_to

from django.forms.models import inlineformset_factory

from django.contrib.auth.models import User

from utils.decorators import enterprise_member_required

from enterprises.models import Enterprise, EnterpriseMember

from projects.forms import NewProjectForm, NewTaskForm
from projects.models import Project, Task


@login_required
@enterprise_member_required()
@render_to('projects/projects_list.html')
def manage_projects(request):
    """
    List the projects for this enterprise
    """
    enterprise = Enterprise.get_from_user_or_404(request.user)
    projects = enterprise.projects.all()
    
    return  locals()
    
@login_required
@enterprise_member_required(owner=True)
@render_to('projects/add_project.html')
def add_project(request):
    """
    Add a new project to a given enterprise
    """
    
    
    enterprise = Enterprise.get_from_user_or_404(request.user)
    
    if request.method == 'POST':
        form = NewProjectForm(enterprise,request.POST)
        if form.is_valid(): 
            new_project = form.save(commit=False)
            new_project.enterprise = enterprise
            new_project.save()     
            form.save_m2m()
            
            
            return redirect('/')
    else:
        form = NewProjectForm(enterprise)


    return locals()



@login_required
@enterprise_member_required()
@render_to('projects/tasks/add_task.html')
def add_task(request,project_id):
    """
    Add a new task to a given project
    """
    
    project = get_object_or_404(Project,pk=project_id)
    
    
    if request.method == 'POST':
        form = NewTaskForm(project,request.POST)
        if form.is_valid(): 
            new_task = form.save(commit=False)
            new_task.project=project
            new_task.save()     
            
            return redirect('/')
    else:
        form = NewTaskForm(project)


    return locals()