from django.db import models
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login
from home.models import User

# Create your views here.

def home(request):
    return HttpResponse('This is homepage.')

def addproduct(request):
    return HttpResponse('This is the page to add products.')

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        query = User.objects.raw("Select count(*) from User where email = '" + email + "' and password = '" + password + "'")
        
        if query == 1:
            #log the user in
            return render(request,'home.html')
        else:
            print("incorrect email or password")
    
    return render(request,'login.html',)


def signup_view(request):
    if request.method == 'POST':
        #storing the data obtained from contact me page in variables.
        name = request.POST['name']
        state = request.POST['state']
        district = request.POST['district']
        town = request.POST['town']
        ward = request.POST['ward']
        prof = request.POST['prof']
        interest = request.POST['interest']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        cnfpassword = request.POST['cnfpassworf']
       #store image file here
        #creating an instance and saving the data to database
        if id(password) == id(cnfpassword):  
            user = User(name=name,add_state=state,add_district=district,add_town=town,add_ward=ward,prof=prof,interest=interest,email=email,phone_number=phone)
            user.save()
            print("data Saved!")
            return render(request,'login.html')
        else:
            print("password don't match")

    return render(request,'signup.html')
    
    
    

def contactus(request):
    return HttpResponse('This is the Contact Us page.')