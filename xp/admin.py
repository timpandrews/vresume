from re import T
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from taggit.models import TaggedItem
from xp.models import Xp, TagType


class XpAdmin(SummernoteModelAdmin):
    list_display = ('id', 'title', 'slug', 'author', 'status',
                    'sort_override', 'created_at', 'updated_at', 'hero_image',)
    list_editable = ('status'),
    list_filter = ('status',)
    search_fields = ['title', 'content']
    list_display_links = ('id', 'title', 'slug',)
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created_at', 'updated_at')
    summernote_fields = ('content')
    verbose_name = 'Xp'

admin.site.register(Xp, XpAdmin)


class TaggedItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag_id', 'tag', 'object_id',
                    'content_object', 'content_type_id', 'content_type')
    list_display_links = ('id', 'tag_id', 'tag', 'object_id',
                          'content_object', 'content_type_id', 'content_type')

admin.site.register(TaggedItem, TaggedItemAdmin)


class TagTypeAdmin(admin.ModelAdmin):
    list_display = ('tag','tag_type')
    list_display_links = ('tag'),
    list_editable = ('tag_type'),
admin.site.register(TagType, TagTypeAdmin)


