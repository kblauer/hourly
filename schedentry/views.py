from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.template import RequestContext

def employee(request):
    return render_to_response('employee.html')

def manager(request):
    return render_to_response('manager.html')