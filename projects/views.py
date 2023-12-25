from django.shortcuts import render
from projects.models import Project


def prokect_index(request):
    # Perform a query that retrieves all objects in the Project database
    # This query returns a collection known as Queryset
    projects = Project.objects.all()

    # Define a dictionnary named context with only one entry: projects to which 
    # we assigned the Queryset containing all the projects
    context = {
        "projects": projects
    }
    return render(request, "projects/projects_index.hmtl", context)

def project_detail(request, pk):
    # The primary key (pk) is the unique identifier of a database entry
    project = Project.objects.get(pk=pk)
    context = {
        "project": project
    }
    return render(request, "projects/project_detail.html", context)