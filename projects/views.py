from django.shortcuts import render, redirect
from projects.models import Project

# Create your views here.


def projects_list(request):
    projects = Project.objects.all()
    context = {
        "projects": projects,
    }
    return render(request, "projects/list.html", context)
