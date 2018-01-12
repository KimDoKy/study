from django import forms
from django.views.generic import ListView, CreateView
from .models import Post

post_list = ListView.as_view(model=Post, paginate_by=3)

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = '__all__'

class PostCreateView(CreateView):
	model = Post
	form_class = PostForm

post_new = PostCreateView.as_view()
