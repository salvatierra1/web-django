from django.db import models

# Create your models here.

class Service(models.Model):
    name = models.CharField(max_length=55)
    description = models.CharField(max_length=500)
    image = models.URLField(max_length=500,blank=True, null=True)
    
    def __str__(self):
        return f"{self.name}, {self.description}"
    