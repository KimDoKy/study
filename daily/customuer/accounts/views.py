from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import get_user_model
from django.shortcuts import render

from .forms import CustomUserCreationForm

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def home(request):
    user = get_user_model()
    return render(request, 'home.html', {'user':user})
