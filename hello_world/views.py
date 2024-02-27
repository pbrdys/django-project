from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello World!")

def another_view(request):
    return HttpResponse("When i say hey you say ho, hey ho hey ho!")