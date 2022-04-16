from django.urls import path, include
from .views import PostView
from rest_framework import routers

route = routers.DefaultRouter()
route.register("", PostView, basename="postapi")

urlpatterns = [
    # path("", PostView.as_view()),
    path("", include(route.urls)),
]
