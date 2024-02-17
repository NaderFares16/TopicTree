from django.shortcuts import render
from .models import Topic
from .forms import TopicForm
from django.http import HttpResponseRedirect
from django.urls import reverse

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

def topic(request, topic_id):
  topic = Topic.objects.get(id = topic_id)
  entries = topic.entry_set.order_by('-date_added')
  context = {
    'topic': topic,
    'entries': entries
  }
  return render(request, 'topic_trees/topic.html', context)

def new_topic(request):
  if request.method != 'POST':
    # EMPTY FORM
    form = TopicForm()
  else:
    # SUBMIT POST DATA
    form = TopicForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect(reverse('topics'))

  context = {'form': form}
  return render(request, 'topic_trees/new_topic.html', context)