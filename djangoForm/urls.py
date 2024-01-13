from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('myForm/', views.myForm, name='myForm'),
    path('modelForm/', views.modelForm, name='modelForm'),
]
