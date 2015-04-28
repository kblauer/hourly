# hourly.views -- contains site wide, app-independent views such as login
# and index.  All other views for site are placed in individual apps,
# which are essentially just directories.  This is the top-level views file.  
# it belongs to no app.  This means that it's specific to hourly, and not modular.

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm
from schedule.models import Schedule
from django.core.mail import send_mail

def contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            errors.append('Enter a subject.')
        if not request.POST.get('message', ''):
            errors.append('Enter a message.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        if not errors:
            send_mail(
                request.POST['subject'],
                request.POST['message'],
                request.POST.get('email','noreply@texasibiz.net'),
                ['admin@texasibiz.net'], #email address where message is sent.
            )
            return HttpResponseRedirect('/thanks/')
    return render(request, 'contact.html',
        {'errors': errors})

def thanks(request):
    return render_to_response('thanks.html')

# This is the Home view, it gets called when the index.html page is requested.  
# All it needs is a username context to fill, if the current user is logged in.
# If they are not, this is None and we can instead prompt the user to login.
def home(request):
    username = None
    
    if request.user.is_authenticated():
        username = request.user.username
    
    args = {}
    args.update(csrf(request))
    
    args['username'] = username
    
    return render_to_response('index.html', args)
    
    # This is the old, insecure way that we were doing this.
    # Keeping it for reference in order to not make the same mistakes
    #return render_to_response('index.html', 
    #                          {'username' : username},
    #                          context_instance=RequestContext(request))
    
def signin (request):
    args = {}
    args.update(csrf(request))
    
    return render_to_response('signin.html', args)
    
def signup (request):
    return render_to_response('signup.html')


# *** Begin User authentication views *** 
def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    
    # query the user database, return either a user object or None
    user = auth.authenticate(username=username, password=password)
    
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/user/success/')
    else:
        return HttpResponseRedirect('/user/invalid/')
    
def success (request):
    return render_to_response('success.html',
                              {'full_name': request.user.username})
    
def invalid_login(request):
    return render_to_response('invalid_login.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


# *** Begin general index page views ***
def about(request):
    username = None
    
    if request.user.is_authenticated():
        username = request.user.username
        
    return render_to_response('about.html', 
                              {'username' : username})
    
    
def services(request):
    username = None
    
    if request.user.is_authenticated():
        username = request.user.username
        
    return render_to_response('services.html', 
                              {'username' : username})


def dashboard(request):
    username = None
    
    if request.user.is_authenticated():
        username = request.user.username
        
        schedules = None
    
        try:
            schedules = Schedule.objects.filter(user = request.user)
            
        except:
            schedules = None
            
    args = {}
    args['username'] = username
    args['schedules'] = schedules
        
    return render_to_response('dash.html', args)
    
def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success')
        
    args = {}
    args.update(csrf(request))
    
    args['form'] = UserCreationForm()
    
    return render_to_response('signup.html', args)

def register_success(request):
    return render_to_response('register_success.html')