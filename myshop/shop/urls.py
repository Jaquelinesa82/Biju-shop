from django.urls import path

from myshop.shop import views

urlpatterns = [
    path('', views.home, name='home'),
]
