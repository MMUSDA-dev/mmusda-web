from django.contrib import admin
from django.contrib.auth.models import Group
from base.models import Description, IndexDescription
from news.models import News


class DescriptionAdmin(admin.ModelAdmin):
    list_display = [ 'title', 'content']

class IndexDescriptionAdmin(admin.ModelAdmin):
    list_display = [ 'title', 'content_key', 'image' ]
    list_filter = ['pub_date', 'pub_by', 'title']
    search_fields = ['title', 'pub_by']

class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'pub_date', 'pub_by']
    list_filter = ['pub_date', 'pub_by']
    search_fields = ['titla', 'pub_by', 'Pub_date']
    

# Register your models here.
admin.site.register(Description, DescriptionAdmin)
admin.site.register(IndexDescription, IndexDescriptionAdmin)
admin.site.register(News, NewsAdmin)
admin.site.site_header = 'North West Kenya Conference of the Seventh-day Adventists'
admin.site.site_title = 'North West Kenya Conference'
admin.site.index_title = 'Dashboard'
admin.site.unregister(Group)