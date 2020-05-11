from django.db import models
from pilot.models import Pilot
from company.models import Company

# Create your models here.
class Inspection(models.Model):
    STATES_ENUM = [
        ('Pendiente', 'Pendiente'),
        ('En Progreso', 'En Progreso'),
        ('Realizada', 'Realizada'),
    ]
    agreed_date = models.DateTimeField()
    performed_date = models.DateTimeField()
    state = models.CharField(choices=STATES_ENUM, max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    pilot = models.ForeignKey(Pilot, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now = False, auto_now_add=True, blank=True, null=True)
    update_date = models.DateTimeField(auto_now = True)
    user_resgister = models.IntegerField(default = 0)