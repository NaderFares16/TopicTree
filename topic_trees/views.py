from django.shortcuts import render
from .models import Topic

def index(request):
  # TOPIC TREE INDEX PAGE
  return render(request, 'topic_trees/index.html')

def topics(request):
  # USER TOPICS PAGE
  topics = Topic.objects.order_by('date_added')
  context = {
    'topics': topics
  }
  return render(request, 'topic_trees/topics.html', context)