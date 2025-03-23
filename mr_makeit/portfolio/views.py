from django.shortcuts import render
from .models import Project
from django.contrib.auth.models import User

def project_list(request):
    projects = Project.objects.all().order_by('-pub_date')
    return render(request, 'portfolio/project_list.html', {'projects': projects})

if not User.objects.filter(username="nyamatwar").exists():
    User.objects.create_superuser("nyamatwar", "snaveford@gmail.com", "Snavedansa@12")

