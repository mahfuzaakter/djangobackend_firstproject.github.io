# from django.conurls import url
from django.urls import path, include
from firstapp import views

urlpatterns = [
    
    path('', views.index, name='index'),
    path('test/', views.contact, name='contact'),
    path('form/',views.form, name='form')

]