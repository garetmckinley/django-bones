from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.template.defaultfilters import slugify
from django.db import models
from django.conf import settings


# Default object model for bones
class BonesObject(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    last_edited = models.DateTimeField(auto_now=True, null=True)

    def __unicode__(self):
        return self.title

    class Meta:
        abstract = True


class BonesProfile(models.Model):
    user = models.OneToOneField(User)
    avatar = models.ImageField(upload_to='avatars')

    def __str__(self):
        return "%s's profile" % self.user


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = BonesProfile.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, sender=User)


class Media(BonesObject):

    """Blog upload class"""
    file = models.ImageField(upload_to='uploads/')
    url = models.URLField(max_length=255, blank=True, null=True)

    def save(self, force_insert=False, force_update=False, using=False):
        self.title = self.file.name
        self.slug = slugify(self.file.name)
        self.url = "%suploads/%s" % (settings.MEDIA_URL, self.file.name)
        super(Media, self).save(force_insert, force_update)

    class Meta:
        verbose_name = "media"
        verbose_name_plural = "media"


# Blog post model
class Post(BonesObject):
    content = models.TextField()
