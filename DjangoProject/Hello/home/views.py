from email import message
from pyexpat.errors import messages
from socket import TCP_NODELAY
from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
# Create your views here.
def index(request):
    # message.success(request,'this is a test message')
    return render(request , 'index.html')
    # return HttpResponse("this is home page")
def about(request):
    return render(request , 'about.html')
    # return HttpResponse("this is about page")
def service(request):
    return render(request , 'services.html')
    # return HttpResponse("this is services page")
def tnontech(request):
    return render(request , 'tnontech.html')
def lnontech(request):
    return render(request , 'lnontech.html')
def ttech(request):
    return render(request , 'ttech.html')
def ltech(request):
    return render(request , 'ltech.html')  
def index1(request):
    return render(request , 'index1.html') 
def intro(request):
    return render(request , 'intro.html') 
def selector(request):
    return render(request , 'selector.html') 
def border(request):
    return render(request , 'border.html') 
def list(request):
    return render(request , 'list.html') 
def position(request):
    return render(request , 'position.html') 
def form(request):
    return render(request , 'form.html') 
def element(request):
    return render(request , 'element.html') 
def imggallery(request):
    return render(request , 'imggallery.html') 
def boxmodel(request):
    return render(request , 'boxmodel.html')                                      
def align(request):
    return render(request , 'align.html')
def comments(request):
    return render(request , 'comments.html')  
def navigation(request):
    return render(request , 'navigation.html')                                  
def contact(request):
    if  request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        

        contact=Contact(name=name,email=email,phone=phone, desc=desc,date=datetime.today()  )
        contact.save()
        # messages.success(request,'Your message has been sent')
    return render(request , 'contact.html')
    # return HttpResponse("this is contact page")    