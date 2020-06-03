from django.contrib import admin
from .models import Topic, Question

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):

	pass

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):

	search_fields = ('topic__slug', 'name')

