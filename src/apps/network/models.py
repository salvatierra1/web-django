from django.db import models

# Create your models here.

class Network(models.Model):
    class IconChoices(models.TextChoices):
        FACEBOOK = 'fa-brands fa-facebook', 'Facebook'
        INSTAGRAM = 'fa-brands fa-instagram', 'Instagram'
        WHATSAPP = 'fa-brands fa-whatsapp', 'Whatsapp'
        
    icon = models.CharField(
        max_length=100,
        choices=IconChoices.choices,
        default=IconChoices.FACEBOOK,
        verbose_name='Icon',
    )
    url = models.URLField(max_length=500, blank=True, null=True)
    
    def __str__(self):
        return f"{self.icon}, {self.url}"
