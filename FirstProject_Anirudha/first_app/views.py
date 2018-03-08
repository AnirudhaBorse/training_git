from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    my_dict={'insert_me': 'INSERTED FROM VIEW','second_key':'AGAIN FROM VIEW'}
    return render(request,'first_app/Index.html',my_dict)

def home(request):
    return HttpResponse("<h1>WELCOME TO THE HOMEPAGE</h1>")