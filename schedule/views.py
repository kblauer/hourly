from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.template import RequestContext
from schedule.models import Schedule
from .forms import ScheduleForm
from schedentry.models import ScheduleEntry
from comments.models import ScheduleComment


def sched_list(request):
    user = request.user
    username = user.username
    
    schedules = None
    managerSchedules = None
    
    try:
        if not user.profile.manager:
            schedules = Schedule.objects.filter(user = user)
        
        elif user.profile.manager:
            managerSchedules = Schedule.objects.filter(user = user.profile.manager)
        
    except:
        schedules = None
    
    
    args = {}
    args['username'] = username
    args['schedules'] = schedules
    args['managerSchedules'] = managerSchedules
    
    return render_to_response('sched_list.html', args)

def getSchedule(request, sched_id):
    username = request.user.username
    
    schedule = Schedule.objects.get(id=sched_id)
    
    args = {}
    args['username'] = username
    args['schedule'] = schedule
    
    return render_to_response('sched_get.html', args)

def createSchedule(request):
    if request.POST:
        form = ScheduleForm(request.POST)
        if form.is_valid():
            survey = form.save(commit=False)
            survey.user = request.user
            survey.save()
            
            return HttpResponseRedirect('/sched/list/')
        
    else:
        form = ScheduleForm()
    
    username = request.user.username
        
    args = {}
    args.update(csrf(request))
    
    args['form'] = form
    args['username'] = username
    
    return render_to_response('createSchedule.html', args)


def editSchedule(request, sched_id):
    
    args = {}
    args.update(csrf(request))
    
    entries = None
    
    try:
        schedule = Schedule.objects.get(pk = sched_id)
        entries = ScheduleEntry.objects.filter(user = request.user, schedule = schedule)
        comments = ScheduleComment.objects.filter(schedule = schedule)
    except:
        entries = None
    
    
    
    args['username'] = request.user.username
    args['schedule'] = get_object_or_404(Schedule, pk=sched_id)
    args['entries'] = entries
    args['comments'] = comments
    
    return render_to_response('calendar_app.html', args)

def employeeView(request, sched_id):
    
    args = {}
    args.update(csrf(request))
    
    entries = None
    
    try:
        schedule = Schedule.objects.get(pk = sched_id)
        entries = ScheduleEntry.objects.filter(user = request.user.profile.manager, schedule = schedule)
        comments = ScheduleComment.objects.filter(schedule = schedule)
    except:
        entries = None
    
    
    
    args['username'] = request.user.username
    args['schedule'] = get_object_or_404(Schedule, pk=sched_id)
    args['entries'] = entries
    args['comments'] = comments
    
    return render_to_response('employee_calendar.html', args)
    