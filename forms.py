from django import forms


class user_form(forms.Form):
    user_name= forms.CharField(label="fullname", widget=forms.TextInput(attrs={'placeholder' : 'enter name'}))
    user_email = forms.EmailField(label="email",widget=forms.TextInput(attrs={'placeholder': 'enter your email address'}))
    user_dob = forms.DateField(label="date of birth", widget= forms.TextInput(attrs={'type': 'date'}))                                                                              