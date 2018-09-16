from rest_framework import generics
from .serializers import BucketSerializer
from .models import Bucket


class CreateView(generics.ListCreateAPIView):
    queryset = Bucket.objects.all()
    serializer_class = BucketSerializer
