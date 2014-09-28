from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.safestring import mark_safe

from bones import functions
from bones.models import Post


def index(request):
    return HttpResponse(
        functions.render_template(request, "index"))


def singlepost(request, post_slug):
    post = Post.objects.get(slug__exact=post_slug)
    body = ""
    if post.css_output:
        body += "<style>%s</style>" % post.css_output
    body += post.content_html
    if post.javascript_output:
        body += "<script type='text/javascript'>%s</script>" % post.javascript_output
    properties = {
        'TITLE': post.title,
        'BODY': mark_safe(body),
        'CATEGORY': post.category,
        'POST_DATE': post.post_date,
        'CREATED_DATE': post.created,
        'LAST_EDIT_DATE': post.last_edited,
    }

    return HttpResponse(
        functions.render_template(request, "singlepost", properties))
