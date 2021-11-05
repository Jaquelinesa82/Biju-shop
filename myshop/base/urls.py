from django.urls import path
from myshop.base import views


urlpatterns = [
    path('', views.home, name='home'),
]
