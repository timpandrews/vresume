from django.contrib import admin

from xp.models import Xp

class XpAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'author', 'status', 'hero_image',)
    list_filter = ('status',)
    search_fields = ['title', 'content']
    list_display_links = ('id', 'title', 'slug',)
    prepopulated_fields = {'slug': ('title',)}
    verbose_name = 'Xp'

admin.site.register(Xp, XpAdmin)
