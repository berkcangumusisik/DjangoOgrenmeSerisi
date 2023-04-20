
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, ),
    path('movies', views.movies),
    path('movies/<slug:slug>', views.movies_details),
    
]
""" 
<slug:slug> ile slug olarak verilen değeri slug değişkenine atıyoruz.
"""
