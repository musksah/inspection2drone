from django.db import models
from inspection.models import Inspection
from drone.models import Drone

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length = 150)
    url = models.TextField()
    type_image = models.CharField(max_length=100)
    size = models.IntegerField()
    weight = models.IntegerField()
    inspection = models.ForeignKey(Inspection, on_delete=models.CASCADE)
    drone = models.ForeignKey(Drone, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now = False, auto_now_add=True, blank=True, null=True)
    update_date = models.DateTimeField(auto_now = True)
    user_resgister = models.IntegerField(default=0)

    class Meta:
        permissions = (
            ("view_dashboard", "Can view dashboard"),
        )
