from django.db import models
from plan.models import Plan

# Create your models here.
class Company(models.Model):
    nit = models.BigIntegerField(unique = True)
    name = models.CharField(max_length = 150)
    email = models.CharField(max_length = 200)
    phone_number = models.IntegerField()
    address = models.CharField(max_length = 250)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    update_date = models.DateTimeField(auto_now = True)
    user_resgister = models.IntegerField(default=0)