from datetime import datetime
import datetime
import json
from time import strptime, mktime

from django.contrib import auth
from django.core import serializers
from django.core.context_processors import csrf
from django.db.transaction import commit
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from schedentry.models import ScheduleEntry
from schedule.models import Schedule
from pip._vendor.cachecontrol import serialize


def all_entry(request, sched_id=1):
    
    user = request.user
    schedule = get_object_or_404(Schedule, id=sched_id)
    
    # Get all of the schedule events associated with this user and their 
    # particular selected calendar
    entries = ScheduleEntry.objects.filter(user = user, schedule = schedule)
    
    # Serialize these elements and return as a JSON object
    entries_serial = serializers.serialize('json', entries)
    response_data = {}
    response_data['response'] = entries_serial
    
    return HttpResponse(json.dumps(response_data), content_type="application/json")


# This view implements an AJAX call in the backend
# which allows for calendar events to be saved.  It takes the 
# data from the browser, fills in the missing parts as per the 
# database schema and then saves the object to the db.
def add_entry(request):
    
    if request.method == 'POST':
        title = request.POST['title']
        start = request.POST['start']
        end = request.POST['end']
        allDay = request.POST['allDay']
        scheduleId = request.POST['scheduleId']
    
        response_data = {}
        
        
        try:
            schedEntry = ScheduleEntry()
            # schedEntry.save(commit=False)
            #import pdb
            #pdb.set_trace()
            
            schedEntry.title = str(title)
            # add the corresponding user and schedule to the schedEntry object
            schedEntry.user = request.user
            schedEntry.schedule = get_object_or_404(Schedule, id=scheduleId)
            
            # format the string date to be a python object
            schedEntry.start = datetime.datetime.fromtimestamp(mktime(strptime(start, "%Y-%m-%d %H:%M:%S")))
            schedEntry.end = datetime.datetime.fromtimestamp(mktime(strptime(end, "%Y-%m-%d %H:%M:%S")))
            
            
            # format the string boolean value
            if allDay == "true":
                schedEntry.allDay = True
            else:
                schedEntry.allDay = False
                
            schedEntry.save()
            
            res_schedule = ScheduleEntry.objects.filter(id=schedEntry.id)
            
            response_data['result'] = 'Success'
            response_data['message'] = serializers.serialize('json', res_schedule)

            
        except:
            response_data['result'] = 'Failure'
            response_data['message'] = "This request failed"
            
        return HttpResponse(json.dumps(response_data), content_type="application/json")
    
def edit_entry(request):
    
    entry_id = request.POST['id']
    
    # Get the schedule entry that the user wants to edit
    schedEntry = get_object_or_404(ScheduleEntry, pk=entry_id)
    
    if request.method == 'POST':
        title = request.POST['title']
        start = request.POST['start']
        end = request.POST['end']
        allDay = request.POST['allDay']
        scheduleId = request.POST['scheduleId']
    
        response_data = {}
        
        try:
            schedEntry.title = str(title)
            # add the corresponding user and schedule to the schedEntry object
            schedEntry.user = request.user
            schedEntry.schedule = get_object_or_404(Schedule, id=scheduleId)
            
            # format the string date to be a python object
            schedEntry.start = datetime.datetime.fromtimestamp(mktime(strptime(start, "%Y-%m-%d %H:%M:%S")))
            schedEntry.end = datetime.datetime.fromtimestamp(mktime(strptime(end, "%Y-%m-%d %H:%M:%S")))
            
            
            # format the string boolean value
            if allDay == "true":
                schedEntry.allDay = True
            else:
                schedEntry.allDay = False
                
            schedEntry.save()
            
            res_schedule = ScheduleEntry.objects.filter(id=schedEntry.id)
            
            response_data['result'] = 'Success'
            response_data['message'] = serializers.serialize('json', res_schedule)

            
        except:
            response_data['result'] = 'Failure'
            response_data['message'] = "This request failed"
            
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def delete_entry(request):
    response_data = {}
    try:
        entry_id = request.POST['id']
        
        # Get the schedule entry that the user wants to edit
        schedEntry = get_object_or_404(ScheduleEntry, pk=entry_id)
        
        schedEntry.delete()
        
        response_data['result'] = 'Success'
        
    except:
        response_data['result'] = 'Failure'
        response_data['message'] = "This request failed"
    
    return HttpResponse(json.dumps(response_data), content_type="application/json")