from django.shortcuts import render
from django.http import HttpResponse

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
    return render(request, 'story.html')

def get_story(request):
    
    story = Controller.getStoryArray(1)
    return HttpResponse(story, content_type='text/plain')

def display_ShowStory(request):

    storyInfo = Controller.parseStoryText(1)

    return HttpResponse(storyInfo, content_type='text/plain')
