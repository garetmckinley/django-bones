from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render
from bones import functions

# Create your views here.


def index(request):
    modernizr = functions.get_modernizr_dict(request)
    template = functions.load_template("index")
    context = RequestContext(request, {
        'TEMPLATE_STATIC': functions.get_template_static(),
        'modernizr': modernizr
    })
    return HttpResponse(template.render(context))
