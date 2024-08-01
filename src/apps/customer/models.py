from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    description = models.CharField(max_length=500)
    mail = models.EmailField(max_length=100)
    phone = models.IntegerField()
    
    def __str__(self):
        return f"{self.name} {self.last_name}"