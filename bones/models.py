from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.template.defaultfilters import slugify
from django.db import models
from django.conf import settings
from scss import Scss
import coffeescript
import markdown


# Default object model for bones
class BonesObject(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    last_edited = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class BonesProfile(models.Model):
    user = models.OneToOneField(User)
    avatar = models.ImageField(upload_to='avatars', null=True)

    def __str__(self):
        return "%s's profile" % self.user


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = BonesProfile.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, sender=User)


class Media(BonesObject):

    """Blog upload class"""
    file = models.FileField(upload_to='uploads/', null=True)
    url = models.URLField(max_length=255, blank=True, null=True)

    def save(self, force_insert=False, force_update=False, using=False):
        self.title = self.file.name
        self.slug = slugify(self.file.name)
        self.url = "%suploads/%s" % (settings.MEDIA_URL, self.file.name)
        super(Media, self).save(force_insert, force_update)

    class Meta:
        verbose_name_plural = "media"


# Blog category model
class Category(BonesObject):

    class Meta:
        verbose_name_plural = "categories"


# Blog post statuses
class Status(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "statuses"


# Bones Content model
class Content(BonesObject):
    status = models.ForeignKey('Status', null=True, default=1)
    status_expression = models.TextField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    content_html = models.TextField(null=True, blank=True)
    yaml_input = models.TextField(null=True, blank=True)
    coffee_input = models.TextField(null=True, blank=True)
    javascript_output = models.TextField(null=True, blank=True)
    scss_input = models.TextField(null=True, blank=True)
    css_output = models.TextField(null=True, blank=True)

    def save(self, force_insert=False, force_update=False, using=False):
        self.javascript_output = coffeescript.compile(self.coffee_input)
        compiler = Scss()
        self.css_output = compiler.compile(self.scss_input)
        self.content_html = markdown.markdown(self.content)
        super(Content, self).save(force_insert, force_update)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


# Blog post model
class Post(Content):
    post_date = models.DateTimeField(null=True)
    category = models.ForeignKey('Category', null=True, default=1)


# Blog page model
class Page(Content):
    pass


# Post template class
class Template(BonesObject):
    jade_input = models.TextField(null=True, blank=True)
    yaml_input = models.TextField(null=True, blank=True)
    coffee_input = models.TextField(null=True, blank=True)
    scss_input = models.TextField(null=True, blank=True)
    html_output = models.TextField(null=True, blank=True)

    def save(self, force_insert=False, force_update=False, using=False):
        js = coffeescript.compile(self.coffee_input)
        compiler = Scss()
        css = compiler.compile(self.scss_input)
        #self.html_output = markdown.markdown(self.content)
        super(Template, self).save(force_insert, force_update)
