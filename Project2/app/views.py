from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Home(request):
    return render (request,'home.html') 
    return HttpResponse('Hello to my Home page')

def Register(request):
    return render (request,'register.html')
    return HttpResponse('Hello to Registration')

def Login(request):
    return render (request,'login.html')
    return HttpResponse('Hello welcome to Login')