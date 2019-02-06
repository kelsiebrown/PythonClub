from django.shortcuts import render, get_object_or_404
from .models import Resource, Meeting

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