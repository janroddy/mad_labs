from django.shortcuts import render
from django.http import HttpResponse

from MadLadParser import Controller

StoryObject = None

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
    global StoryObject
    StoryObject = Controller.Controller(1)
    story = StoryObject.getStoryArray()
    return HttpResponse(story, content_type='text/plain')

def send_input(request):

    output = StoryObject.injectWords(request.data)
    return HttpResponse(output, content_type='text/plain')

def display_ShowStory(request):

    storyInfo = StoryObject.parseStoryText()

    return HttpResponse(storyInfo, content_type='text/plain')
