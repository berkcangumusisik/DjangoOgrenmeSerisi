from django.http.response import HttpResponseNotFound
from django.shortcuts import redirect, render
from django.urls import reverse
import datetime
data = {
    "telefon":["Samsung S21", "Samsung S21 Ultra", "Samsung S21 Plus", "Samsung S21 FE", "Samsung S21 5G"],
    "bilgisayar":["Asus","Lenovo"],
    "elektronik":[]
}

def index(request):
    
    categories= list(data.keys())
    return render(request, 'index.html',{"categories":categories})

def getProductsByCategoryId(request, category_id):
    category_list = list(data.keys())

    if category_id > len(category_list):
        return HttpResponseNotFound("yanlış kategori seçimi")
        
    category_name = category_list[category_id-1]
    
    redirect_path = reverse("products_by_category", args= [category_name])
    
    return redirect(redirect_path)

def getProductsByCategory(request, category):
    
        products = data[category]        
        return render(request, 'products.html', {
            "category": category,
            "products": products,
            "now" : datetime.datetime.now()
        })
    


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
"""


""" 

"""