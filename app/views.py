from django.shortcuts import render
from django.http import HttpResponse, response, Http404
from django.views.generic import ListView, DeleteView
from .models import Topic, Question

from django.views.decorators.http import require_http_methods

@require_http_methods(['GET'])
def search_topic(request):
	q = request.GET.get('q')
	if q:
		topic = Topic.objects.filter(topic__icontains=q)
		return render(request, 'app/search_topic.html', {'topic': topic, 'query': q})
	return render(request, 'app/empty_search.html')

class TopicList(ListView):

	model = Topic
	paginate_by = 100
	# template_name = 'app/file.html'

def question(request, slug):
	try:
		questions = Question.objects.filter(topic__slug=slug).all()
		topic = Topic.objects.get(slug=slug)
	except Question.DoesNotExist:
		raise Http404('questions does not exist')
	return render(request, 'app/topic_questions_detail.html', {'questions': questions, 'topic': topic})

