from django.db import models
from authr.models import User

# Create your models here.
class Pilot(models.Model):
    name = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    address = models.CharField(max_length=250)
    birthdate = models.DateTimeField()
    phonenumber = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now = False, auto_now_add=True, blank=True, null=True)
    update_date = models.DateTimeField(auto_now = True)
    user_register = models.IntegerField(default=0)

    class Meta:
        permissions = (
            ("view_profile", "Can view profile"),
        )