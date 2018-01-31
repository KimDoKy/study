from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from .models import Post
from .serializers import PostSerializer


class PostListAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs) 

# /post/10/ => GET, PUT, DELETE
class PostDetailAPIView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):

	queryset = Post.objects.all()
	serializer_class = PostSerializer

	def get(self, request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs)

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)
	
	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)

from rest_framework import status
from .models import Post
from .serializers import PostSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def post_list(request):
	if request.method == 'GET':
		serializer = PostSerializer(Post.objects.all(), many=True)
		return Response(serializer.data)
	else:
		serializer = PostSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=201)
		return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)

	if request.method == 'GET':
	    serializer = PostSerializer(post)
	    return Response(serializer.data)
	elif request.method == 'PUT':
	    serializer = PostSerializer(post, data=request.data)
	    if serializer.is_valid():
		    serializer.save()
		    return Response(serializer.data)
	    return Response(serializer.errors, status=400)
	else:
		post.delete()
		return Response(status=204)
