from django.shortcuts import render

from django.http import HttpResponse

def book2(request):
    return HttpResponse('<h1>Twisted Series<h1/>')

# Create your views here.
