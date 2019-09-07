from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer
from .permissions import IsAuthor


class CreateView(generics.ListCreateAPIView):
    '''
    Sampel Rest API 제공 

    ---
    테스트입니다.
    '''

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,
                          IsAuthor)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class DetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,
                          IsAuthor)
