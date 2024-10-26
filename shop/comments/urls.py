from os import name
from django.urls import path
from . import views


app_name = 'review'

urlpatterns = [
    path('', views.ReviewView.as_view(), name='reviews'),
    path('create/', views.CreateReviewView.as_view(), name='create-review')
]