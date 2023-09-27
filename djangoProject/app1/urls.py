from django.urls import path
from .import views 

urlpatterns=[
     path("", views.index,name="index"),
    path("<str:name>",views.greet, name="greet")
    
    # path("ragnar",views.ragnar, name="ragnar"),

   # path("<str:name>",views.greet,name="greet")


]
