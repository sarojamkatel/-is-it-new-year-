from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1 style="color:blue">if this thing gets printed then it worked <h1>')

def saroj(request):
      return render  (request , "app1/index.html")
# def ragnar(request):
#     return HttpResponse("hello ragnar")

# #this makes more flexible
# def greet(request,name):
#     return HttpResponse(f"hello, {name}!")

def greet( request , name ):
     return render(request ," app1/greet.html",{"name":name.capitalize()})


