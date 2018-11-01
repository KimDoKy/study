from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Team, CustomUser

class AccountListView(ListView):
    models = CustomUser
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context

    def get_queryset(self):
        qs = CustomUser.objects.all()
        return qs
