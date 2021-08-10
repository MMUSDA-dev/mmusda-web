from django.db import models


# Create your models here.
class Description(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    class Meta:
        verbose_name_plural = ' About page contents'

class IndexDescription(models.Model):
    title = models.CharField(max_length=200)
    content_key = models.TextField()
    content_extra = models.TextField()
    pub_date = models.DateField('date Published', null=True)
    pub_by = models.CharField('Published By', max_length=200, blank=True)
    image = models.ImageField(upload_to= 'media/')

    class Meta:
        verbose_name_plural = 'Home page contents'
    
    def __str__(self):
        return self.title