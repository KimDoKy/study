from rest_framework import generics, permissions
from .permissions import IsOwner
from .serializers import TodoSerializer
from .models import Todo

class CreateView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (permissions.IsAuthenticated,IsOwner)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class DetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (permissions.IsAuthenticated,IsOwner)
