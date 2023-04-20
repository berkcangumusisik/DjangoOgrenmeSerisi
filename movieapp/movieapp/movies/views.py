from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "index.html")


def movies(request):
    return render(request, "movies.html")


def movies_details(request, slug):
    return render(request, "movies_details.html", {"slug": slug})
