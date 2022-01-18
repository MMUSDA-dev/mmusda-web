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

class CarouselContent(models.Model):
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField()
    
    class Meta:
        verbose_name_plural = 'Carousel'
        
    def __str__(self):
        return self.title

class TestimonialData(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    image = models.ImageField()

    class Meta:
        verbose_name_plural = 'Testimonies'

    def __str__(self):
        return self.title

