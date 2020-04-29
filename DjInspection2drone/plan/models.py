from django.db import models

# Create your models here.
class Plan(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField()
    photos_number = models.IntegerField()
    user_number = models.IntegerField()
    analysis_number = models.IntegerField()
    term_months_number = models.IntegerField()
    inspection_number = models.IntegerField(default=0)
   