from django.shortcuts import render
from django.http import HttpResponse
from firstapp.models import musician, album

# Create your views here.


def index(request):
    musician_list = musician.objects.order_by('first_name')
    diction={'text_1':'this a list of musician','musician':musician_list}
    # return HttpResponse("hello World <a href='contact/'> contact </a> <a href='about/'> about </a>")
    return render(request, 'firstapp/index.html', context=diction)
def contact(request):
    return HttpResponse("this is contact page <a href='/'> index </a> <a href='/about/'> about </a>")

def about(request):
    return HttpResponse("<h1>About us</h1> <a href='/'> index </a> <a href='/contact/'> contact </a>")