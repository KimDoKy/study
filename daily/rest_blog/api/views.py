from rest_framework import generics, permissions
from blog.models import Post
from blog.serializers import PostSerializer
from blog.permissions import IsAuthor

class CreateView(generics.ListCreateAPIView):
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
