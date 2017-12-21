from django.db import models
from django.utils import timezone

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=100)
	order = models.PositiveSmallIntegerField()
	private_state = models.BooleanField(default=False)

	def private(self):
		self.private_state = not self.private
		self.save()

	def __str__(self):
		return self.name

class Post(models.Model):
	author = models.ForeignKey('auth.User')
	category = models.ForeignKey('blog.Category')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		slef.save()
	
	def __str__(self):
		return self.title
