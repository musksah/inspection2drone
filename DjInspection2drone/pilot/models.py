from django.db import models

# Create your models here.
class Pilot(models.Model):
    name = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    address = models.CharField(max_length=250)
    birthdate = models.DateTimeField()
    phonenumber = models.IntegerField()
    start_date = models.DateTimeField(auto_now = False, auto_now_add=True, blank=True, null=True)
    update_date = models.DateTimeField(auto_now = True)
    user_resgister = models.IntegerField(default=0)