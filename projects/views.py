from django.shortcuts import render
from projects.models import Project
from projects.models import SmallerProjects

def project_index(request):
    projects = Project.objects.all()
    smallerProjects = SmallerProjects.objects.all()
    context = {
        'projects': projects,
        'smaller_projects': smallerProjects
    }
    return render(request, 'project_index.html', context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project,
    }
    return render(request, 'project_detail.html', context)

def small_project_detail(request, pk):
    smallerProjects = SmallerProjects.objects.get(pk=pk)  
    context = {
        'smaller_projects': smallerProjects
    }
    return render(request, 'smallproject_detail.html', context)