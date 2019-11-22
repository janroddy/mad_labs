from django.shortcuts import render

from .models import Story

from MadLadParser import Controller

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

    #story = Story.objects.get(pk=1).story_array
    #story = "noun,verb,adjective,name"
    story = Controller.getStoryArray(1)

    return render(request, 'story.html', {'Story' : story})
