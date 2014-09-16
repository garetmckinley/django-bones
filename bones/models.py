from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db import models


# Default object model for bones
class BonesObject(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
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


# Blog post model
class Post(BonesObject):
    content = models.TextField()
