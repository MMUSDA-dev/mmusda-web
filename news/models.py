from django.db import models
from departments.models import Department
from django.db.models.deletion import CASCADE


# Create your models here.
class blogcontent(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    subtitle = models.CharField(max_length=200, blank=True)
    content = models.TextField()
    department = models.ForeignKey(Department, on_delete=CASCADE)
    img = models.ImageField()
    pub_date = models.DateField('date Published')
    pub_by = models.CharField('Published By', max_length=200, blank=True)
    
    class Meta:
        verbose_name_plural = 'News'


    