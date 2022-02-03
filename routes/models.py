from django.db import models

# Create your models here.
class Route(models.Model):
    route_name = models.CharField(max_length=255)
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    distance=models.FloatField(default=0.0)
    condition=models.BooleanField(default=False)
    cost=models.FloatField(default=0.0)

    def __str__(self) -> str:
        return self.route_name