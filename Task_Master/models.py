from django.db import models
import datetime

class task_data(models.Model):
    title=models.CharField(max_length=100,unique=True)
    date=models.DateField(default=datetime.datetime.now)
    completed=models.BooleanField(null=True,blank=True)