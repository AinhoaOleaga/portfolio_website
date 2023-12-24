from django.db import models


# In django a class in models is a database
# We want to create a databse that contains 3 fields:
# title -> a short string to hold the name of the project, description -> a larger string to contain a
# piece of texte, technology -> a string field but its contentes will be limited to a select nbr of choices

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
