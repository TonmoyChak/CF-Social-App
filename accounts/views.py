from django.shortcuts import render
from django.urls import reverse,reverse_lazy #reverse_lazy for log in or log out where they should go
# Create your views here.
from django.views.generic import CreateView
from . import forms


class SignUp(CreateView):
    form_class = forms.UserCreationForm
    success_url  = reverse_lazy('login')
    template_name = 'accounts/signup.html'
