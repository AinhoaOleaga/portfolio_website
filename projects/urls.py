from django.urls import path
from projects import views

urlpatterns = [
    path("", views.prokect_index, name="project_index"),
    path("<int:pk>/", views.project_detail, name="project_detail"), #Dynamic creation of urls using the pk of each projects
    
]
