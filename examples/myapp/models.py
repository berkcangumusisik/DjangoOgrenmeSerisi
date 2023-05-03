from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.CharField(max_length=200)
    imageUrl = models.CharField(max_length=200)
""" 
Model : Veritabanı tablolarını temsil eder.
models.Model : Model sınıfından türetilir.
models.CharField : Karakter dizisi tutar.
models.DecimalField : Ondalıklı sayı tutar.
max_digits : Ondalıklı sayının kaç basamaklı olacağını belirtir.
decimal_places : Ondalıklı sayının ondalık kısmının kaç basamaklı olacağını belirtir.
Migration : Model sınıfı değiştiğinde veritabanında değişiklik yapmak için kullanılır. python manage makemigrations ile migration dosyası oluşturulur. python manage.py migrate ile migration dosyası veritabanına uygulanır.

python manage.py shell : Django ile birlikte gelen bir komuttur. Django projesi içerisinde python kodları yazmamızı sağlar.
Shell içerisinde model sınıflarını kullanmak için from <app>.models import <model> şeklinde import ederiz.
Ürün eklemek için product = Product(product_name="Samsung S21", price=10000, description="Samsung S21", imageUrl="https://productimages.hepsiburada.net/s/45/550/11093652097074.jpg") şeklinde tanımlarız.
p3.save() ile veritabanına kaydederiz.
"""
