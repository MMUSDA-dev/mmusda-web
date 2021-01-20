from django.contrib import admin
from base.models import Description


class DescriptionAdmin(admin.ModelAdmin):
    list_display = [ 'title', 'content']

# Register your models here.
admin.site.register(Description, DescriptionAdmin)