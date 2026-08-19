from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

"""
def function(http request):
    return http response

"""


#  mysite.com/hello -> Hello World
# set url path in urls.py urlpatterns list
def hello_world_view(request):
    return HttpResponse("Hello World")


def hello_python_view(request):
    return HttpResponse("Hello Python")


# Render HTML page
def hello_html_view(request):
    # return render(request, <html file path>)
    # html file has to be in path ./templates/<app name>
    return render(request, "todos/hello.html")


# you get parameters from a url from urlpattern
# path("helloname/<str:name>", views.hello_path_view, name="hello_name"),
def hello_path_view(request, name):
    return HttpResponse(f"Hello {name}!")


def add_view(request, num1, num2):
    return HttpResponse(f"Sum is {num1 + num2}")
