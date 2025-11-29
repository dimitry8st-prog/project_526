from django.shortcuts import render
from django.http import HttpResponse

def home_view(requst):
    return HttpResponse("Главная страница")
