from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render
from bones import functions

# Create your views here.


def index(request):
    modernizr = functions.getModernizrDict(request)
    template = functions.loadTemplate("index")
    context = RequestContext(request, {
        'TEMPLATE_STATIC': functions.getTemplateStatic(),
        'modernizr': modernizr
    })
    return HttpResponse(template.render(context))
