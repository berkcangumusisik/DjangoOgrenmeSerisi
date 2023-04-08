from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('details', views.details, name='details'),
    path('<int:category_id>', views.getProductsByCategoryId ),
    path('<str:category>', views.getProductsByCategory),
]

"""
path() fonksiyonu ile url tanımlanır. İlk parametre url adresi, ikinci parametre ise hangi fonksiyonun çalışacağıdır.
Path() sırası da önemlidir.
"""
