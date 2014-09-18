# forms.py
from django import forms
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string

from bones.models import Post


class PostVueWidget(forms.Textarea):

    class Media:
        css = {
            'all': ('bones/admin/vue_widget/style.css',
                    'bones/admin/vue_widget/github-markdown.css',)
        }
        js = (
            'bones/lib/jquery-1.11.1.min.js',
            'bones/lib/marked.min.js',
            'bones/lib/vue.min.js',
            'bones/admin/vue_widget/init.js',
        )


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=PostVueWidget)

    class Meta:
        model = Post
