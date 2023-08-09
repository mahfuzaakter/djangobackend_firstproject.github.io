from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    diction={'text_1':'i am a text from views.py'}
    # return HttpResponse("hello World <a href='contact/'> contact </a> <a href='about/'> about </a>")
    return render(request, 'firstapp/index.html', context=diction)
def contact(request):
    return HttpResponse("this is contact page <a href='/'> index </a> <a href='/about/'> about </a>")

def about(request):
    return HttpResponse("<h1>About us</h1> <a href='/'> index </a> <a href='/contact/'> contact </a>")