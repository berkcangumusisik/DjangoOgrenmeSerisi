from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('index', views.index),
    path('create', views.create),
    path('update/<int:id>', views.update, name='product_update'),
    path('delete/<int:id>', views.delete, name='delete_update'),
    path('list', views.list, name='product_list'),
    path('<slug:slug>', views.details, name='product_details'),
]
"""
path() fonksiyonu ile url tanımlanır. İlk parametre url adresi, ikinci parametre ise hangi fonksiyonun çalışacağıdır.
Path() sırası da önemlidir.
"""

