from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

"""
def function(http request):
    return http response

"""


#  mysite.com/hello -> Hello World
def hello_world_view(request):
    return HttpResponse("Hello World")


def hello_python_view(request):
    return HttpResponse("Hello Python")
