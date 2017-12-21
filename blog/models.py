from django.db import models

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=100)
	order = models.IntegerField()
	private_state = models.BooleanField(default=False)

	def private(self):
		self.private_state = not self.private
		self.save()

	def __str__(self):
		self.name
