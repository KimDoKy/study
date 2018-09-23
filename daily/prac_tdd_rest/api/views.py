from rest_framework import generics
from .serializers import TodoSerializer
from .models import Todo

class CreateView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
