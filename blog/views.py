from django.views.generic import ListView
from .models import Category

class PostList(ListView):
	template_name = 'blog/post_list.html'
	queryset = Category.objects.filter(private_state=False)
	context_object_name = 'categorys'
