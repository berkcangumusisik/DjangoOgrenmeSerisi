from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import redirect
from django.urls import reverse
data = {
    "telefon": "Telefon Kategorisindeki Ürünler",
    "bilgisayar": "Bilgisayar Kategorisindeki Ürünler",
    "elektronik": "Elektronik Kategorisindeki Ürünler"
}


def index(request):
    list_items = "<h1>Ürünler</h1>"
    category_list = list(data.keys())
    for category in category_list:
        redirect_path = reverse("products_by_category", args=[category])
        list_items += f"<li> <a href='{redirect_path}'>{category}</a> </li>"
    response_data = f"<ul>{list_items}</ul>"
    return render(request, "index.html" )


def getProductsByCategoryId(request, category_id):
    category_list = list(data.keys())
    if category_id > len(category_list):
        return HttpResponseNotFound("Sayfa Bulunamadı")
    category_name = category_list[category_id-1]

    redirect_path = reverse("products_by_category", args=[category_name])
    return redirect(redirect_path)


def getProductsByCategory(request, category):
    try:
        category_text = data[category]
        return render(request, "products.html", {"category": category.capitalize(), "category_text": category_text})
    except:
        return HttpResponseNotFound("Sayfa Bulunamadı")


"""
HttpResponse : Django ile birlikte gelen bir fonksiyondur. İçerisine yazılan değeri ekrana basar.
Dinamik path tanımlamak için : <degiskenAdi> şeklinde tanımlanır. Fonksiyon içerisinde bu değişkeni kullanabiliriz.

HttpResponseRedirect : Bir url adresine yönlendirme yapar. 
redirect() fonksiyonu ile de aynı işlemi yapabiliriz.
HttpResponseNotFound : Sayfa bulunamadı hatası verir.
reverse() : url tanımlarını kullanmak için kullanılır. İlk parametre url adı, args parametresi ise url içerisindeki değişkenleri gönderir.
Html tagları ile birlikte HttpResponse kullanılabilir.
"""
