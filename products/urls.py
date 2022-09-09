from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.ProductsBehaviour.as_view()),
    path('add/', views.AddProduct.as_view()),
]
