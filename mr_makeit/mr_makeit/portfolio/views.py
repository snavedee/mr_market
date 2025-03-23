from django.shortcuts import render
from .models import Project

def project_list(request):
    projects = Project.objects.all().order_by('-pub_date')
    return render(request, 'portfolio/project_list.html', {'projects': projects})