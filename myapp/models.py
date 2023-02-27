from django.db import models
from django.conf import settings
from django.utils import timezone


class employee(models.Model):
    name=models.CharField(max_length=50)
    designation=models.CharField(max_length=50)
    salary=models.IntegerField()
    mobile_no=models.IntegerField()
    create_date=models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name

# Create your models here.
