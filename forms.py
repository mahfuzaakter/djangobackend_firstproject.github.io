from django import forms
from django.core.validators import MaxLengthValidator
from django.core import validators


# validation
def even_or_not(value):
    if value%2 == 1:
        raise forms.ValidationError("please insert an even number")
    
class user_form(forms.Form):
    user_name= forms.CharField(label="fullname", widget=forms.TextInput(attrs={'placeholder' : 'enter name'}))
    user_email = forms.EmailField(label="email",widget=forms.TextInput(attrs={'placeholder': 'enter your email address'}))
    user_dob = forms.DateField(label="date of birth", widget= forms.TextInput(attrs={'type': 'date'}))                                                                              
    
    boolean_field= forms.BooleanField()
    char_field= forms.CharField(max_length=15, min_length=5,required=False)
    choice_field=forms.ChoiceField(choices=(('','--select option--'),('1','first'),('2','second')))
    choices=(('a','a'),('b','b'),('c','c'))

    # validator er jonno
    # name= forms.CharField(validators==[.MaxLengthValidator(10)])
    name = forms.CharField(validators=[MaxLengthValidator(10)])
    num= forms.IntegerField(validators=[even_or_not])

    