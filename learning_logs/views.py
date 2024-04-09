from django.shortcuts import render

# Create your views here.

def index(request):
    """HomePage"""
    return render(request, 'learning_logs/index.html')