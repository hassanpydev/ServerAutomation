# configure django app urls
from django.urls import path
from .views import index

urlpatterns = [
    path("", index),
]
