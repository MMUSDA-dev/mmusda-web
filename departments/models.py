from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=200)

class Department_head(models.Model):
    name = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=CASCADE)

