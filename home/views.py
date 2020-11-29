from django.shortcuts import render , HttpResponse
from home import models
from datetime import datetime
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        "variable":"This is manas Chandan Behera"
    }
    #messages.success(request, "This is a test Message")
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
        messages.success(request, "Your form Has been Submitted . Thank You !")
    return render(request , "contact.html")

def services(request):
    return render(request , "services.html")
