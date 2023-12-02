from django.http import HttpResponse
from django.shortcuts import render


def Home(request):
    # your code here
    return render(request , "index.html")

def InnerPage(request):
    # your code here
    return render(request , "inner-page.html")

def ProtFolio(request):
    # your code here
    return render(request , "portfolio-details.html")