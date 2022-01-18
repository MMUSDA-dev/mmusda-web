from django.contrib import admin
from django.contrib.auth.models import Group
from base.models import Description, IndexDescription, CarouselContent, TestimonialData
from news.models import blogcontent
from departments.models import Department, Department_head

class DescriptionAdmin(admin.ModelAdmin):
    list_display = [ 'title', 'content']

class IndexDescriptionAdmin(admin.ModelAdmin):
    list_display = [ 'title', 'content_key', 'image' ]
    list_filter = ['pub_date', 'pub_by', 'title']
    search_fields = ['title', 'pub_by']

class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'pub_date', 'pub_by']
    list_filter = ['pub_date', 'pub_by']
    search_fields = ['title', 'pub_by', 'Pub_date']
    prepopulated_fields = {'slug': ('title',)}


    

# Register your models here.
admin.site.register(Description, DescriptionAdmin)
admin.site.register(IndexDescription, IndexDescriptionAdmin)
admin.site.register(blogcontent, NewsAdmin)
admin.site.register(CarouselContent)
admin.site.register(TestimonialData)
admin.site.register(Department)
admin.site.register(Department_head)

#admin panel header settings
admin.site.site_header = 'Seventh-day Adventist Church Multimedia University'
admin.site.site_title = 'MMUSDA'
admin.site.index_title = 'Dashboard'
admin.site.unregister(Group)