from django.urls import path
from pages import views

# List of URL patterns corresponding the different view functions
urlpatterns = [
    path("", views.home, name='home'),
]