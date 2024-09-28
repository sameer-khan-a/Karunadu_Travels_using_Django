
from cmath import phase
from django.contrib import messages
import email
from django.shortcuts import HttpResponse, render
from datetime import datetime
from home.models import Contact, Register

# Create your views here.


def index(request):


    return render(request, 'index.html')


    # return HttpResponse("this is homepage")

def about(request):
     return render(request, 'about.html')

def services(request):
    return render(request, 'services.html') 

def register(request):
    if request.method == "POST":
        Name = request.POST.get('Name')
        Address = request.POST.get('Address')
        email = request.POST.get('email')
        Package = request.POST.get('Package' )
       
        register = Register(Name=Name , Address=Address, email=email, Package=Package )
        register.save()
        messages.success(request, 'Registration Successful!!!')
    return render(request, 'register.html')        

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc' )
       
        contact = Contact(name=name , email=email, phone=phone, desc=desc )
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')  




         

       
   