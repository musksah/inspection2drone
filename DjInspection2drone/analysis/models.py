from django.db import models
from image.models import Image

# Create your models here.
class Analysis(models.Model):
    date = models.DateTimeField()
    result = models.TextField()
    report = models.TextField()
    image = models.ForeignKey(Image, on_delete=models.CASCADE, default=1)
    start_date = models.DateTimeField(auto_now = False, auto_now_add=True, blank=True, null=True)
    update_date = models.DateTimeField(auto_now = True)
    user_resgister = models.IntegerField(default=0)


