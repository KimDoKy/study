from rest_framework import generics
from .models import Bucketlist
from .serializers import BucketlistSerializer


class CreateView(generics.ListCreateAPIView):
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer

    def perform_create(self, serializer):
        serializer.save()

