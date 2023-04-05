from django.shortcuts import render

def index():
    return HttpResponse("Merhaba")

"""
HttpResponse : Django ile birlikte gelen bir fonksiyondur. İçerisine yazılan değeri ekrana basar.
"""

