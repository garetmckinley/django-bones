# forms.py
from django import forms
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string

from bones.models import Post


class PostVueWidget(forms.Textarea):

    class Media:
        css = {
            'all': ('bones/lib/jquery-ui/jquery-ui.theme.css',
                    'bones/lib/jquery-ui/jquery-ui.min.css',
                    'bones/admin/vue_widget/style.css',
                    'bones/admin/vue_widget/github-markdown.css',)
        }
        js = (
            'bones/lib/jquery-1.11.1.min.js',
            'bones/lib/jquery-ui/jquery-ui.min.js',
            'bones/lib/marked.min.js',
            'bones/lib/vue.min.js',
            'bones/admin/vue_widget/init.js',
        )


class AceWidget(forms.Textarea):

    def __init__(self, label, lang, field):
        super(AceWidget, self).__init__()
        self.Media.langs.append(lang)
        self.Media.labels.append(label)
        self.Media.fields.append(field)
        langs = "+".join(self. Media.langs)
        fields = "+".join(self.Media.fields)
        labels = "+".join(self.Media.labels)
        self.Media.js += ('bones/admin/ace_widget/init.js?lang=%s&field=%s&label=%s' % (
            langs, fields, labels),)

    class Media:
        langs = []
        fields = []
        labels = []
        js = (
            'bones/lib/ace/ace.js',
        )


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=PostVueWidget, required=False)
    yaml_input = forms.CharField(
        widget=AceWidget("YAML", "yaml", "yaml_input"), required=False)
    coffee_input = forms.CharField(
        widget=AceWidget("Coffee", "coffee", "coffee_input"), required=False)
    scss_input = forms.CharField(
        widget=AceWidget("SCSS", "scss", "scss_input"), required=False)
    status_expression = forms.CharField(
        widget=AceWidget("Status Expression", "python", "status_expression"), required=False)

    class Meta:
        model = Post
