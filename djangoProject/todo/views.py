from django.shortcuts import render

tasks = ["ohoo", " hoho", " haha"]

# Create your views here.

def todo(request):
    return render(request , "todo/index.html",{"list":tasks})

#now create template HTML files inside todo app

