from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("GIDER DU IKKE GODT AT VIRKE!")
