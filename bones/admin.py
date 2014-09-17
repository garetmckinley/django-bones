from django.contrib import admin
from bones.models import BonesObject, Post, BonesProfile, Media, Category


class BonesObjectAdmin(admin.ModelAdmin):

    """Default ModelAdmin for BonesObject"""
    prepopulated_fields = {"slug": ("title",)}


class MediaAdmin(admin.ModelAdmin):

    """Default ModelAdmin for BonesObject"""
    list_display = ('preview', 'title', 'url', 'created')
    prepopulated_fields = {"slug": ("title",)}

    def preview(self, obj):
        return "<img src='%s' height='45'>" % obj.url
    preview.allow_tags = True
    preview.short_description = 'Preview'


# Register your models here.
admin.site.register(Media, MediaAdmin)
admin.site.register(Category, BonesObjectAdmin)
admin.site.register(Post, BonesObjectAdmin)
admin.site.register(BonesProfile)
