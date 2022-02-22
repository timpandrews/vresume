from django.contrib import admin

from xp.models import Xp

class XpAdmin(admin.ModelAdmin):
    list_display = ('id', 'placeholder', 'hero_image')
    list_display_links = ('id', 'placeholder')
    verbose_name = "Xp"

admin.site.register(Xp, XpAdmin)
