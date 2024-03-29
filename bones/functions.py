from django.template import RequestContext, loader
from django.utils.safestring import mark_safe
from django.conf import settings
import re
import urllib


def load_template(file):
    template = loader.get_template('%s/%s.jade' % (settings.BONES_TEMPLATE,
                                                   file))
    return template


def which_template():
    return settings.BONES_TEMPLATE


def get_template_static():
    return '%sbones/templates/%s' % (settings.STATIC_URL, which_template())


def get_template_file_path(file):
    path = '%s/%s.jade' % (which_template(), file)
    return path


def render_template(request, template, properties={}):
    modernizr = get_modernizr_dict(request)

    wrapper = load_template("wrapper")
    template = load_template(template)

    properties['TEMPLATE_STATIC'] = get_template_static()
    properties['modernizr'] = modernizr

    context = RequestContext(
        request, properties)
    subtemplate = template.render(context)

    wrapper_context = RequestContext(
        request,
        {
            'PAGE_CONTENT': subtemplate,
            'TEMPLATE_STATIC': get_template_static(),
            'modernizr': modernizr,
        })
    return wrapper.render(wrapper_context)


def get_modernizr_dict(request):
    try:
        get = request.COOKIES.get('modernizr')
        url = urllib.parse.unquote(get)

    except:
        return {}

    values = re.split('=|&', url)
    modernizr = {}
    keys = [x for ind, x in enumerate(values) if ind % 2 == 0]
    values = [x for ind, x in enumerate(values) if ind % 2 != 0]
    s = []
    for x in range(0, len(keys)):
        subvalues = re.findall(r"\[([A-Za-z0-9_]+)\]", keys[x])
        if len(subvalues) > 0:
            subvalue = subvalues[0]
            key = keys[x].replace("[%s]" % subvalue, "")
            try:
                modernizr[key][subvalue] = int(values[x])
            except:
                modernizr[key] = {subvalue: int(values[x])}
        else:
            key = keys[x]
            modernizr[key] = int(values[x])
    return modernizr


def set_default_settings(defaults):
    for attr, value in defaults.items():
        if not hasattr(settings, attr):
            setattr(settings, attr, value)


def permalink(category, slug):
    return '/%s/%s/' % (category, slug)


def make_link(url, text):
    return mark_safe('<a href="%s">%s</a>' % (url, text))
