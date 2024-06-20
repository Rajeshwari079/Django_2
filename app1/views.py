from django.shortcuts import render

from django.http import HttpResponse

def book1(request):
    return HttpResponse('<h1>Divergent<h1/>')

# Create your views here.
