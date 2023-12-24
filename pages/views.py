from django.shortcuts import render

# pages/views.py

# Define a view function named home
# When this function is called it'll render an HTML file named home.html
def home(request):
    return render(request, "pages/home.html", {})
