from django.db import models
from django.template.defaultfilters import slugify

class Topic(models.Model):

	topic = models.CharField(max_length=100, unique=True)
	created = models.DateTimeField(auto_now_add=True)
	slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)

	def __str__(self):
		return self.topic

	def save(self, *args, **kwargs):
		self.slug = slugify(self.topic)
		super(Topic, self).save(*args, **kwargs)

class Question(models.Model):

	topic = models.ForeignKey(Topic, related_name='question', on_delete=models.CASCADE)
	name = models.CharField(max_length=650)

	def __str__(self):
		return '< Topic: {} > {} '.format(self.topic, self.name)