from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	#pass in function instead of calling it right now
	date_posted = models.DateTimeField(default=timezone.now)
	#if user is deleted, delete post
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	#dunder method
	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk':self.pk})