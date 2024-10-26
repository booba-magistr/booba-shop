from os import name
from django.urls import path
from . import views

app_name = "order"

urlpatterns = [path('create-order/', views.CreateOrderView.as_view(), name='create_order'),
               path("success-order/", views.SuccessOrder.as_view(), name="success_order")]
