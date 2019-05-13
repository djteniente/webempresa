
from django.urls import path
from . import views     

urlpatterns = [
    #Path del core
    path('', views.home, name="index"),
    path('about/', views.about, name="about"),
    path('store/', views.store, name="store"),
    path('contact/', views.contact, name="contact"),
    path('sample/', views.sample, name="sample"),
]
