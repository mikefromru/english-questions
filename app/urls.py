from django.urls import path, re_path
from . import views

urlpatterns = [
	path('', views.TopicList.as_view(), name='list-topic'),
	path('detail/<slug:slug>/', views.question, name='questions-topic'),
    re_path(r'^search/?$', views.search_topic, name='search-topic'),

]
