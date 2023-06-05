from django.urls import path
from projects.views import projects_list, detail_projects

urlpatterns = [
    path("", projects_list, name="list_projects"),
    path("<int:id>/", detail_projects, name="show_project"),
]
