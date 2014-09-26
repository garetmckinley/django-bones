from django.conf.urls import patterns, url

from bones import views
from bones.models import Page, Category
urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
)

templates = Page.objects.filter()

for template in templates:
    additional_settings = patterns(
        '',
        (r'^template/' + template.slug + '/$', 'template'),
    )
    urlpatterns += additional_settings


categories = Category.objects.all()

for category in categories:
    additional_settings = patterns(
        '',
        url(r'^' + category.slug + '/(?P<post_slug>.*)/$',
            views.singlepost, name='singlepost'),
    )
    urlpatterns += additional_settings

print(urlpatterns)
