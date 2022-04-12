from posixpath import basename
from xml.etree.ElementInclude import include
from django.urls import path
from .views import PostView
from rest_framework import routers

route = routers.DefaultRouter()

route.register("", PostView, basename="pos.post")

urlpatterns = [
    path("", PostView.as_view()),
    path("", include(route.urls)),
]
