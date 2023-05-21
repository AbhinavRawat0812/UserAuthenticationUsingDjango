from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Hello World") 


def validateLogin(request):
    
    class user:
        cust_id:int
        cust_name:int

    user.cust_id=1
    user.cust_name=2

    return HttpResponse(user.cust_name)