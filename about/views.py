from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def about_index(request):
    if request.method == "POST":
        return HttpResponse("You must have posted sth")
    else:
        return HttpResponse(request.method)