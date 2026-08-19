from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotAllowed

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


# query
# helloquery/?query=value
def hello_query_view(request):
    # return HttpResponse(<access request arg>)
    return HttpResponse(f"Your query was {request.GET.get("query")}")


# redirect. import from django.shortcuts
def redirect_view(request):
    # do stuff
    # return redirect(<view name>)
    return redirect("hello_html")


# post_example
def post_endpoint_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        job = request.POST.get("job")

        return HttpResponse(f"You posted: {name = }, {age = }, {job =}")
    else:
        return HttpResponseNotAllowed(["POST"])
