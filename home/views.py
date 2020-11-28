from django.shortcuts import render , HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("This is my home page")

def about(request):
    return HttpResponse("this is the abut page")

def contact(request):
    return HttpResponse("this is the contact page")

def services(request):
    return HttpResponse("These are services page")
