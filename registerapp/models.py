from django.db import models

# Create your models here.

class registermodel(models.Model):
    name = models.CharField(unique=True, max_length=50)
    password = models.CharField( max_length=50)
    email = models.EmailField(max_length=254, unique=True)
        