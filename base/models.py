from django.db import models


# Create your models here.
class Description(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=255)

    verbose_plural = 'Description'
