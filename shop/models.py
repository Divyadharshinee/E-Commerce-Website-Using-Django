from django.db import models

# Create your models here.

class Task(models.Model):
    task = models.CharField(max_length=120,null=False,blank=False)
    assingned_to= models.CharField(max_length=50,null=True,blank=True)

