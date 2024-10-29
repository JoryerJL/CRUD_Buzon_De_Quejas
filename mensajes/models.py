from django.db import models

# Create your models here.
class Mensaje(models.Model):
    mensaje = models.CharField(max_length=100)
    fecha   = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.mensaje
