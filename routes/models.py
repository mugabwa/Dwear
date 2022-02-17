from enum import auto
from django.db import models

# Create your models here.
class Route(models.Model):
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    distance=models.CharField(max_length=100)
    condition=models.BooleanField(default=False)
    cost=models.FloatField(default=0.0)

    def __str__(self) -> str:
        return "From: "+self.origin+"To: "+self.destination 

class RouteData(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    filepath = models.FileField(upload_to='files/', null=True, verbose_name='')
    uploaded_at = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self) -> str:
        return str(self.route)