from django.urls import path

from . import views

urlpatterns = [
    path("hello", views.hello_world_view, name="hello_world"),
    path("", views.hello_python_view, name="hello_python"),
    path("htmlrender/", views.hello_html_view, name="hello_html"),
    path("helloname/<str:name>", views.hello_path_view, name="hello_name"),
    path("redirect/", views.redirect_view, name="redirect"),
    path("add/<int:num1>/<int:num2>", views.add_view, name="add"),
    path("helloquery/", views.hello_query_view, name="hello_query"),
    path("postendpoint/", views.post_endpoint_view, name="post_example"),
]
