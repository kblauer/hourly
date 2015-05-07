from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from comments.models import ScheduleComment
from schedule.models import Schedule

# Create your views here.
def addComment(request):
    if request.POST:
        try:
            comment = ScheduleComment()
            comment.user = request.user
            comment.schedule = get_object_or_404(Schedule, id=request.POST['schedule'])
            comment.comment = request.POST['comment']
            
            comment.save()
            
            return HttpResponseRedirect('/sched/empview/' + request.POST['schedule'])
        
        except:
            return HttpResponseRedirect('/sched/empview/' + request.POST['schedule'])
            