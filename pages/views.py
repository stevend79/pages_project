from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def homePageView(request):
    return HttpResponse("<h1>Homepage</h1>")

def aboutPageView(request):
    return HttpResponse("<h1>About Page</h1><p>This is the about page.</p>")
