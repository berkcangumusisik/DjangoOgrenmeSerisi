
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name ="home_page"),
    path('movies', views.movies, name="movies_page"),
    path('movies/<slug:slug>', views.movies_details, name="movies_details"),
    
]
""" 
<slug:slug> ile slug olarak verilen değeri slug değişkenine atıyoruz.
"""
