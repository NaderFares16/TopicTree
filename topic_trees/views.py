from django.shortcuts import render

def index(request):
  # TOPIC TREE INDEX PAGE
  return render(request, 'topic_trees/index.html')
