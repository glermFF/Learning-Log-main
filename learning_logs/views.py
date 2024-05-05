from django.shortcuts import render, redirect
from .models import Topic
from .forms import TopicForm, EntryForm
# Create your views here.

def index(request):
    """HomePage"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Show Topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """Show each topic and all entries"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topics.html', context)

def new_topic(request):
    """Add New Topic"""
    if request.method != 'POST': # No data, return a blank form;
        form = TopicForm()
    else: # Data submitted, process data
        form = TopicForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('learning_logs:topics')
    
    context = {'form':form}
    return render(request, 'learning_logs/new_topic.html', context)

def new_entry(request, topic_id):
    """Add New Entry"""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST': # No data, create new blank form;
        form = EntryForm()
    else: # Data submitted, process data;
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)
        
    context = {'topic':topic, 'form':form}
    return render(request, 'learning_logs/new_entry.html', context)