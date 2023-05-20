from django.shortcuts import render
# reverse_lazy is use when the user is login or logout where they should go
from django.urls import reverse_lazy
from . import form
# CreateView use to make django make the view
from django.views.generic import CreateView
# Create your views here.


class SingUp(CreateView):
    form_class = form.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = 'accounts/signup.html'
