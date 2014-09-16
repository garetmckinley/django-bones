from django.contrib import admin
from bones.models import BonesObject, Post, BonesProfile


class BonesObjectAdmin(admin.ModelAdmin):
    """Default ModelAdmin for BonesObject"""
    prepopulated_fields = {"slug": ("title",)}


# Register your models here.
admin.site.register(Post, BonesObjectAdmin)
admin.site.register(BonesProfile)
