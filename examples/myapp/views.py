from django.http import Http404, HttpResponseRedirect
from django.http.response import HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
import datetime
from .models import Product
from django.db.models import Avg, Min, Max
from .forms  import ProductForm

# data = {
#     "telefon":["Samsung S21", "Samsung S21 Ultra", "Samsung S21 Plus", "Samsung S21 FE", "Samsung S21 5G"],
#     "bilgisayar":["Asus","Lenovo"],
#     "elektronik":[]
# }

def index(request):
    products = Product.objects.filter(isActive = True).order_by("product_name")
    context = {
        "products":products,
    }
    return render(request, 'index.html',context)
def details(request, slug):
    
    product = get_object_or_404(Product, slug = slug)
    context = {"product":product}
    return render(request, 'details.html', context)

def list(request):
    if 'q' in request.GET and request.GET.get('q'):
        q = request.GET['q']
        products = Product.objects.filter(name__contains=q).order_by("product_name")
    else:
        products = Product.objects.all().order_by("product_name")
        
    context={
            "products":products,
        }
    return render(request, 'list.html', context)

def create(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("product_list")
        else:
            form = ProductForm()
    form = ProductForm()
    
    return render(request, 'create.html', {"form":form})

def update(request, id):
    product = get_object_or_404(Product, pk = id)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("product_list")
    else:
        form = ProductForm(instance=product)
    return render(request, 'update.html', {"form":form})

def delete(request, id):
    product = get_object_or_404(Product, pk = id)

    if request.method == "POST":
        Product.objects.get(pk=id).delete()
        return redirect("product_list")
    return render(request, 'delete-confirm.html', {"product":product})
"""
HttpResponse : Django ile birlikte gelen bir fonksiyondur. İçerisine yazılan değeri ekrana basar.
Dinamik path tanımlamak için : <degiskenAdi> şeklinde tanımlanır. Fonksiyon içerisinde bu değişkeni kullanabiliriz.

HttpResponseRedirect : Bir url adresine yönlendirme yapar.
redirect() fonksiyonu ile de aynı işlemi yapabiliriz.
HttpResponseNotFound : Sayfa bulunamadı hatası verir.
reverse() : url tanımlarını kullanmak için kullanılır. İlk parametre url adı, args parametresi ise url içerisindeki değişkenleri gönderir.
Html tagları ile birlikte HttpResponse kullanılabilir.

Html içinde for kullanmak için {% %} kullanılır.
endfor ile for döngüsünün sonunu belirtiriz. Onu da {% endfor %} içinde kullanırız.

if kullanmak için {% %} kullanılır. {% endif %} ile if bloğunun sonunu belirtiriz. products|length ile products listesinin uzunluğunu alırız.

| : pipe işareti ile birbirinden farklı işlemler yapabiliriz. Örneğin products|length ile products listesinin uzunluğunu alırız.

block : html içerisinde bir bloğu tanımlamak için kullanılır. {% block content %} {% endblock %} şeklinde kullanılır.

{% include "dosya" %} : html içerisinde başka bir html dosyasını çağırırız.

Local Static Files : settings.py içerisinde STATIC_URL tanımlarız. STATICFILES_DIRS içerisinde dosyaların bulunduğu dizini tanımlarız. {% load static %} ile static dosyaları kullanabiliriz. {% static "dosya" %} ile dosyaları çağırırız.
CSS ve JS dosyalarını kullanmak için {% load static %} ile static dosyaları kullanabiliriz. {% static "dosya" %} ile dosyaları çağırırız.

python manage.py superuser : admin paneline giriş yapmak için kullanılır.


FORM İŞLEMLERİ
- request.GET : formdan gelen verileri alır.
- __contains : içerisinde arama yapar.
- request.POST : formdan gelen verileri alır. HTTP POST kullanma nedenimiz, verileri url üzerinde göstermemek içindir.
- CSRF : Cross Site Request Forgery. Formdan gelen verilerin güvenliğini sağlar. settings.py içerisindeki MIDDLEWARE kısmında bulunur. {% csrf_token %} ile form içerisinde kullanılır.
- Request.GET.get() : formdan gelen verileri alır. Eğer veri yoksa None döner.

Form Class
- Form class'ı oluşturmak için forms.Form kullanılır.
- Form class'ı içerisinde tanımlanan alanlar, form içerisindeki alanlara karşılık gelir.
- required olarak tanımlanan alanlar, form içerisinde zorunlu olarak doldurulması gereken alanlardır.
- max_length ile alanların maksimum uzunluğunu belirleriz.
- min_length ile alanların minimum uzunluğunu belirleriz.
- decimal_places ile alanların ondalık kısmının kaç basamak olacağını belirleriz.

- widget=forms.Textarea ile alanların textarea olarak görünmesini sağlarız.
- label ile form içerisindeki alanların isimlerini belirleriz.

form.as_p : form içerisindeki alanları p etiketleri içerisinde gösterir.
form.as_ul : form içerisindeki alanları ul etiketleri içerisinde gösterir.
"""

