from django.db import models
from django.utils.text import slugify
class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.name}"
class Address(models.Model):
    street = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.street} - {self.postal_code} - {self.city}"
class Supplier(models.Model):
    company_name = models.CharField(max_length=50)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return f"{self.company_name}"

class Product(models.Model):
    product_name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.CharField(max_length=200)
    imageUrl = models.CharField(max_length=200)
    isActive = models.BooleanField(default=True)
    slug = models.SlugField(default="", blank = True,null=False, db_index=True, unique=True)
    categories = models.ManyToManyField(Category)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f"{self.product_name} - {self.price}"
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



Sorgu Örnekleri
Product.objects.all() : Tüm ürünleri getirir.
Prduct.objects.get(pk = <number>) : Primary key değerine göre ürün getirir.

Filtreleme İşlemi 
Entry.objects.filter() : Belirtilen koşula uyan tüm kayıtları getirir. virgül ile birden fazla koşul belirtilebilir.

Or Operatorü : 
from django.db.models import Q ile Q nesnesi import edilir.
Entry.objects.filter(Q(kosul1) | Q(kosul2)) şeklinde kullanılır.

Veri Güncelleme
p3 = Product.objects.get(pk=3)
p3.price = 9000

Veri Silme
p3.delete()

db_index : Veritabanında index oluşturur.
unique : Veritabanında unique index oluşturur.
slugify : Verilen string değerini url uyumlu hale getirir.


One to Many İlişki
Bir model sınıfı başka bir model sınıfına ForeignKey ile bağlanır. ForeignKey alanı bir başka model sınıfının Primary Key alanını tutar.

models.ForeignKey(Category, on_delete=models.CASCADE) : Category model sınıfının Primary Key alanını tutar. Category model sınıfı silindiğinde bu alana sahip Product model sınıfı silinir.

models.ManyToManyField() : Çoktan Çoka ilişkiyi temsil eder.
"""
