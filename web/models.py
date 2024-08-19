from django.db import models

class Index(models.Model):
    nameProject = models.CharField(max_length=100)
    descriptionProject = models.TextField()
    imageProject = models.ImageField(upload_to='images/', null=True, blank=True)

   





    

