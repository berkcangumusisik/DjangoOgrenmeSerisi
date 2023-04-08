from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import redirect
data = {
    "telefon" : "Telefon Kategorisindeki Ürünler",
    "bilgisayar" : "Bilgisayar Kategorisindeki Ürünler",
    "elektronik" : "Elektronik Kategorisindeki Ürünler"
}
def index(request):
    return HttpResponse("Index")

def details(request):
    return HttpResponse("Detaylar")


def getProductsByCategoryId(request, category_id):
    category_list = list(data.keys())
    if category_id > len(category_list):
        return HttpResponseNotFound("Sayfa Bulunamadı")
    redirect_text = category_list[category_id-1]
    return redirect("/products/"+redirect_text)

def getProductsByCategory(request, category):
    try:
        category_text = data[category]
        return HttpResponse(category_text)
    except:
        return HttpResponseNotFound("Sayfa Bulunamadı")


"""
HttpResponse : Django ile birlikte gelen bir fonksiyondur. İçerisine yazılan değeri ekrana basar.
Dinamik path tanımlamak için : <degiskenAdi> şeklinde tanımlanır. Fonksiyon içerisinde bu değişkeni kullanabiliriz.

HttpResponseRedirect : Bir url adresine yönlendirme yapar. 
redirect() fonksiyonu ile de aynı işlemi yapabiliriz.
HttpResponseNotFound : Sayfa bulunamadı hatası verir.
"""

