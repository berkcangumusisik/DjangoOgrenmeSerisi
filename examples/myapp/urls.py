from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
]

"""
path() fonksiyonu ile url tanımlanır. İlk parametre url adresi, ikinci parametre ise hangi fonksiyonun çalışacağıdır.
"""