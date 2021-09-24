from django.shortcuts import render, get_object_or_404
from .models import Project

def home(request):
    projects = Project.objects.all()
    return render(request, 'projects/home.html', {
        'projects': projects,
    })

def detail(request, job_id):
    job_detail = get_object_or_404(Project, pk=job_id)
    return render(request, 'projects/detail.html', {
        'job_detail' : job_detail,
    })