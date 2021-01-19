from django.db import models


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True)
    description = models.TextField
    pub_date = models.DateField('date Published')
    pub_by = models.CharField(max_length=200, blank=True)