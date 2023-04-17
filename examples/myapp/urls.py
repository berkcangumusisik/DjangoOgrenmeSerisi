from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('index', views.index),
    path('<int:category_id>', views.getProductsByCategoryId),
    path('<str:category>', views.getProductsByCategory, name='products_by_category')
]
"""
path() fonksiyonu ile url tanımlanır. İlk parametre url adresi, ikinci parametre ise hangi fonksiyonun çalışacağıdır.
Path() sırası da önemlidir.
"""

