from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home (request):
    return HttpResponse("Hello, this is homepage.")


def profile (request):
    return HttpResponse("This is profile page.")