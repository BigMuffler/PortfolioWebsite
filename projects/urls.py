from django.urls import path
from . import views


urlpatterns = [
    path("", views.project_index, name="project_index"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
    path("small/<int:pk>/", views.small_project_detail, name="smallproject_detail"),
]
