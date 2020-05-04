from django.db import models

# Create your models here.
class Drone(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    line = models.CharField(max_length=100)
    serialnumber = models.CharField(max_length=250)
    weight = models.IntegerField()
    flight_time = models.IntegerField()
    start_date = models.DateTimeField(auto_now = False, auto_now_add=True, blank=True, null=True)
    update_date = models.DateTimeField(auto_now = True)
    user_resgister = models.IntegerField(default=0)

class Drone_Element(models.Model):
    name = models.CharField(max_length = 150)
    brand = models.CharField(max_length = 150)
    amount = models.IntegerField()
    serialnumber = models.CharField(max_length=250)
    color = models.CharField(max_length = 100)
    drone = models.ForeignKey(Drone, on_delete=models.CASCADE)
