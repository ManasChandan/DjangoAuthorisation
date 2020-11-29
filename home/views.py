from django.shortcuts import render , HttpResponse

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
    return render(request , "contact.html")

def services(request):
    return render(request , "services.html")
