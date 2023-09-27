from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    return render(request ,"app2/index.html",{"newyear":true})
# this will return true if and only if today is new year's day







