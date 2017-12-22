from django.utils import timezone
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from .models import Category
from .models import Post

class Categorys(ListView):
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['categorys'] = Category.objects.filter(private_state=False).order_by('order')
		return context

class Home(Categorys):
	teplate_name = 'blog/post_list.html'
	context_object_name = 'posts'

	def get_queryset(self):
		return Post.objects.filter(category__private_state=False).filter(published_date__lte=timezone.now()).order_by('published_date')

class PostList(Home):

	def get_queryset(self):
		self.category = get_object_or_404(Category, name=self.kwargs['category'])
		return Post.objects.filter(category__private_state=False).filter(category__name=self.category).filter(published_date__lte=timezone.now()).order_by('published_date')
