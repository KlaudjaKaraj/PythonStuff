from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def shop_home(request):
    return HttpResponse("This is shop homepage")