from django.db import models



class Route(models.Model):
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    distance = models.CharField(max_length=100)
    condition = models.BooleanField(default=False)
    cost = models.FloatField(default=0.0)
    filepath = models.FileField(upload_to='files/', null=True, blank=True, verbose_name='')
    calculated_cost = models.FloatField(default=0.0)
    cost_status = models.BooleanField(default=False)

    def __str__(self) -> str:
        return "From: " + self.origin + "To: " + self.destination
