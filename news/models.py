from django.db import models


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True)
    content = models.TextField()
    pub_date = models.DateField('date Published')
    pub_by = models.CharField('Published By', max_length=200, blank=True)

    class Meta:
        verbose_name_plural = 'News'


    