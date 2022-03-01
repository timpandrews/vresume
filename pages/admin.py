from django.contrib import admin

from pages.models import Resume

class ResumeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'filename')
    list_display_links = ('id', 'name')

admin.site.register(Resume, ResumeAdmin)
