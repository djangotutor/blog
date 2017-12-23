from django.utils import timezone
from django.views.generic.base import RedirectView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .models import Category
from .models import Post
from .forms import PostForm

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
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['category_name'] = self.kwargs['category']
		return context

class PostDetail(DetailView):
	model = Post
	template_name = 'blog/post_detail.html'
	context_object_name = 'post'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['categorys'] = Category.objects.filter(private_state=False).order_by('order')
		context['category_name'] = Category.objects.filter(post__id=self.kwargs['pk'])[0].name
		return context

class PostNew(CreateView):
	model = Post
	fields = ['category', 'title', 'text']
	template_name = 'blog/post_edit.html'

	def form_valid(self, form):
		post = form.save(commit=False)
		post.author = self.request.user
		return super().form_valid(form)

class PostEdit(UpdateView):
	model = Post
	fields = ['category', 'title', 'text']
	template_name = 'blog/post_edit.html'

	def form_valid(self, form):
		post = form.save(commit=False)
		post.author = self.request.user
		return super().form_valid(form)

class PostDraftList(ListView):
	template_name = 'blog/post_draft_list.html'
	context_object_name = 'posts'
	queryset = Post.objects.filter(published_date__isnull=True).order_by('created_date')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['categorys'] = Category.objects.filter(private_state=False).order_by('order')
		return context

class PostPublish(RedirectView):
	permanent = False
	query_string = True
	pattern_name = 'post_detail'

	def get_redirect_url(self, *args, **kwargs):
		post = get_object_or_404(Post, pk=kwargs['pk'])
		post.publish()
		return super().get_redirect_url(*args, **kwargs)

class PostRemove(DeleteView):
	model = Post
	success_url = reverse_lazy('home')
