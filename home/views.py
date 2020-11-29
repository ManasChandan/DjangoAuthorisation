from django.shortcuts import render , HttpResponse
from home import models
from datetime import datetime

# Create your views here.
def index(request):
    context = {
        "variable":"This is manas Chandan Behera"
    }
    return render(request , "index.html" , context)
    # CDN - Content Delivery Network
    # return HttpResponse("This is my home page")

def about(request):
    return render(request , "about.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        dsc = request.POST.get('dsc')
        cont = models.contact(name=name, email=email, phone=phone, dsc=dsc, date=datetime.today())
        cont.save()
    return render(request , "contact.html")

def services(request):
    return render(request , "services.html")
