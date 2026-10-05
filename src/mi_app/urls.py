from django.urls import path
from .views import sumar_view

urlpatterns = [
    path('sumar/', sumar_view, name='sumar'),
]