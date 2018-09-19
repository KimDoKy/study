from rest_framework import generics
from .models import Bucket
from .serializers import BucketSerializer


class CreateView(generics.ListCreateAPIView):
    queryset = Bucket.objects.all()
    serializer_class = BucketSerializer


class DetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bucket.objects.all()
    serializer_class =BucketSerializer
