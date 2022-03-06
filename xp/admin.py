from django.contrib import admin

from xp.models import Xp

class XpAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'author', 'status', 'created_at', 'updated_at', 'hero_image',)
    list_filter = ('status',)
    search_fields = ['title', 'content']
    list_display_links = ('id', 'title', 'slug',)
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created_at', 'updated_at')
    verbose_name = 'Xp'

admin.site.register(Xp, XpAdmin)
