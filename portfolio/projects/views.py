from django.shortcuts import render
from .models import Project

def home(request):
    projects = Project.objects.all()
    return render(request, 'projects/home.html', {
        'projects': projects,
    })

def detail(request, job_id):
    return render(request, 'projects/detail.html')