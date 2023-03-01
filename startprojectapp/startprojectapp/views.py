import sys, traceback, cgi
from django.shortcuts import render

from django.http import HttpResponseServerError
from django.template import loader, Context, RequestContext

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)

def page_error_500_view(request, *args, **argv):

    t = loader.get_template('500.html')
    trace = traceback.format_exc()
    type, value, tb = sys.exc_info()

    filename = tb.tb_frame.f_code.co_filename
    name = tb.tb_frame.f_code.co_name
    line_no = tb.tb_lineno

    return render(request, '500.html', {
        'type': type.__name__,
        'trace': trace,
        'value': value
    })
