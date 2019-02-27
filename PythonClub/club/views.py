from django.shortcuts import render, get_object_or_404
from .models import Resource, Meeting
from .forms import ResourceForm, MeetingForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'club/index.html')

def resources (request):
    type_list=Resource.objects.all()
    return render (request, 'club/resources.html', {'type_list': type_list})

def meetings (request):
    meetings_list = Meeting.objects.all()
    return render (request, 'club/meetings.html', {'meetings_list': meetings_list})

def meetingdetail (request, id):
    detail = get_object_or_404(Meeting, pk=id)
    context = {'detail': detail}
    return render (request, 'club/details.html', context=context)

# resource form view
@login_required
def newResource(request):
    form=ResourceForm
    if request.method=='POST':
        form=ResourceForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ResourceForm()
    else:
        form=ResourceForm()
    return render(request, 'club/newresource.html', {'form': form})

# meeting form view
@login_required
def newMeeting(request):
    form=MeetingForm
    if request.method=='POST':
        form.MeetingForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form.MeetingForm()
    else:
        form=MeetingForm()
    return render(request, 'club/newmeeting.html', {'form': form})

#login/logout functionality
def loginmessage(request):
    return render(request, 'club/loginmessage.html')

def logoutmessage(request):
    return render(request, 'club/logoutmessage.html')