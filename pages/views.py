from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_page_view(request):
    return HttpResponse("<h1><center>Hello Mustafa!</center></h1>")