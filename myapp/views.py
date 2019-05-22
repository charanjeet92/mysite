import datetime
from django.shortcuts import render,redirect
from django.template import loader

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from myapp.form import EmpForm


def index(request):
    stu = EmpForm()
    return HttpResponse(render())

@require_http_methods(["GET"])
def charan(request):
    return HttpResponse('<h1> cahran.</h1>')
def hello(request):
    now = datetime.datetime.now()
    html = "<html><body><h3>Now time is %s.</h3></body></html>" % now
    return HttpResponse(html)

def show(request):
    template = loader.get_template('index.html') # getting our template
    name = {
        'student':'rahul'
    }
    return HttpResponse(template.render(name))


def second(request):
    template = loader.get_template('second.html')
    return HttpResponse(template.render())
