from os import name
from django.urls import path
from . import views


urlpatterns = [
    path("", views.Index.as_view(), name="home"),
    path("about/", views.StuffView.as_view(), name="about"),
    path('contact/', views.ContactView.as_view(), name='contact'),
]
