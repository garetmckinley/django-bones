from django import template
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.utils.text import Truncator

from bones.models import Post, BonesProfile
from bones import functions

import datetime
import re
from markdown import markdown


register = template.Library()


@register.simple_tag
def post_loop(max_posts):
    posts = Post.objects.filter(
        status__title="Published").order_by('-post_date')[:max_posts]

    output = ""

    for x in range(0, len(posts)):
        post = posts[x]
        permalink = functions.permalink(post.category, post.slug)
        summary = Truncator(post.content_html)
        properties = {
            "TITLE": post.title,
            "TITLE_LINK": functions.make_link(permalink, post.title),
            "BODY": mark_safe(summary.words(100, html=True)),
            "CATEGORY": post.category,
            "POST_DATE": post.post_date,
            "CREATED_DATE": post.created,
            "LAST_EDIT_DATE": post.last_edited,
        }
        output += render_to_string(
            functions.get_template_file_path("postloop"), properties)

    return output
