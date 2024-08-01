from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    image = models.URLField(max_length=500,blank=True, null=True)
    phone = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    hour = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.name},{self.description}"
    