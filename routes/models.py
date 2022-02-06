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