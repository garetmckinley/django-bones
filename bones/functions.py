from django.template import RequestContext, loader
from django.conf import settings
import re
import urllib


def loadTemplate(file):
    template = loader.get_template('%s/%s.jade' % (settings.BONES_TEMPLATE,
                                                   file))
    return template


def whichTemplate():
    return settings.BONES_TEMPLATE


def getTemplateStatic():
    return '%sbones/templates/%s' % (settings.STATIC_URL, whichTemplate())


def getModernizrDict(request):
    try:
        get = request.COOKIES.get('modernizr')
        url = urllib.unquote(get).decode('utf8')
    except:
        return {}

    values = re.split('=|&', url)
    modernizr = {}
    keys = [x for ind, x in enumerate(values) if ind % 2 == 0]
    values = [x for ind, x in enumerate(values) if ind % 2 != 0]
    s = []
    for x in xrange(0, len(keys)):
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
