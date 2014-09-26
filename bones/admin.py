from django.contrib import admin
from bones.models import (
    BonesObject, Post, BonesProfile, Media, Category, Page,
    Template, Menu)
from bones.forms import PostForm, WidgetForm


class BonesObjectAdmin(admin.ModelAdmin):

    """Default ModelAdmin for BonesObject"""
    prepopulated_fields = {"slug": ("title",)}
    form = WidgetForm

    def save_model(self, request, obj, form, change):
        print("SAVING MODEL")
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.last_editor = request.user
        obj.save()


class MediaAdmin(admin.ModelAdmin):

    """Default ModelAdmin for BonesObject"""
    list_display = ('preview', 'title', 'url', 'created')
    prepopulated_fields = {"slug": ("title",)}

    def preview(self, obj):
        return "<img src='%s' height='45'>" % obj.url
    preview.allow_tags = True
    preview.short_description = 'Preview'


class PostAdmin(BonesObjectAdmin):

    """PostAdmin is a subclass of BonesObjectAdmin"""
    fieldsets = (
        (None, {
            'fields': ('title',
                       'slug',
                       'category',
                       'status',
                       'post_date',
                       'status_expression',
                       'content',
                       )
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('yaml_input',
                       'coffee_input',
                       'scss_input',
                       )
        }),
    )
    form = PostForm


class PageAdmin(BonesObjectAdmin):

    """PostAdmin is a subclass of BonesObjectAdmin"""
    fieldsets = (
        (None, {
            'fields': ('title',
                       'slug',
                       'status',
                       'status_expression',
                       'content',
                       )
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('yaml_input',
                       'coffee_input',
                       'scss_input',
                       )
        }),
    )
    form = PostForm


# Register your models here.
admin.site.register(Media, MediaAdmin)
admin.site.register(Template, BonesObjectAdmin)
admin.site.register(Menu, BonesObjectAdmin)
admin.site.register(Category, BonesObjectAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(BonesProfile)
