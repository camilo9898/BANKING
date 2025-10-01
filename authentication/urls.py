from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
]
urlpatterns = [
    path("", views.country, name="country"),
]
urlpatterns = [
    path("", views.city, name="city"),
]