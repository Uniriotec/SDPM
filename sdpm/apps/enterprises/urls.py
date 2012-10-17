'''
Created on 17/10/2012

@author: arruda
'''
from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('enterprises.views',
#    url(r'^$', 'index'),
#    url(r'^exibir/(?P<template_id>\d+)/$', 'exibir',name='exibir_avaliacao'),    
    url(r'^register/$', 'register',name='register_enterprise'),  
)
