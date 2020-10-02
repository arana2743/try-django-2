from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    title="Learning Django 2.2!!!"
    return render(request, "index.html", {'title': title})
    
