# -*- coding: utf-8 -*-

from django.contrib.auth import login
from django.shortcuts import redirect, get_object_or_404
from annoying.decorators import render_to

from enterprises.forms import RegistrationForm

from django.contrib.auth.models import User

@render_to('user/register.html')
def register(request): 
    
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid(): 
            
            return redirect('/thanks/')
    else:
        form = RegistrationForm()

    return locals()

