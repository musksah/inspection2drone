from django.db import models
from company.models import Company
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
