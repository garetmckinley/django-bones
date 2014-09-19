from django.conf.urls import patterns, url

from bones import views
from bones.models import Page
urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
)

templates = Page.objects.filter()
print(templates)
for template in templates:
    additional_settings = patterns(
        '',
        (r'^template/' + template.slug + '/$', 'template'),
    )
    urlpatterns += additional_settings
