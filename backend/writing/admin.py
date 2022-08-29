from django.contrib import admin
from .models import Writing

# Register your models here.
class WritingAdmin(admin.ModelAdmin):
    list_display = ['title', 'board']
    list_display_links = ['title', 'board']
admin.site.register(Writing, WritingAdmin)
