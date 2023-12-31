from django.shortcuts import render
from django.http import HttpResponse
from firstapp.models import musician 
from firstapp import forms

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

def form(request):
    
    # new1_form= forms.musicianForm()
    new1_form= forms.musicianForm()
    new_form = forms.user_form() 
    dictionary={'test_form': new_form, 'text':'this form created django    '}
    
    if request.method == 'post' :
        new1_form= forms.musicianForm(request.POST)
        if new1_form.is_valid():
            new1_form.save(commit=True)
            return index(request)
        
        new_form=forms.user_form(request.post)
        dictionary.update({'test_form':new_form})
        if new_form.is_valid():
            user_name =new_form.cleaned_data['user_name']
            user_dob= new_form.cleaned_data['user_dob']
            user_email= new_form.cleaned_data['user_email']
                                                                                                                                                                       
            dictionary.update({' user_name':user_name})
            dictionary.update({'user_dob':user_dob})
            dictionary.update({'user_email':user_email})
            dictionary.update({'form_submit':"yes"})
            
            
            dictionary.update({'boolean_field':new_form.cleaned_data['boolean_field']})
            dictionary.update({'char_field':new_form.cleaned_data['char_data']})
            dictionary.update({'num ':new_form.cleaned_data['num']})
    dictionary={'test_form':new1_form,'heading_1':'Add new musician'}
    return render(request, 'firstapp/form.html', context=dictionary)