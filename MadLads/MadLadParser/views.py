from django.shortcuts import render

from .models import Story

# Create your views here.
def display_home(request):
    return render(request, 'index.html')

def display_about(request):
    return render(request, 'about.html')

def display_categories(request):
    return render(request, 'categories.html')

def display_howToPlay(request):
    return render(request, 'how-to-play.html')

def display_story(request):

    story = {"noun,verb,adjective,name"}
    return render(request, 'story.html', {'Story' : story})
