from django.urls import path
from projects.views import projects_list

urlpatterns = [
    path("", projects_list, name="list_projects"),
]
