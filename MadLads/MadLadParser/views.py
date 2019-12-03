from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from MadLadParser import Story
from MadLadParser import Controller

StoryObject = None
Controller = Controller.Controller()

# Create your views here.
def display_home(request):
    return render(request, 'index.html')

def display_about(request):
    return render(request, 'about.html')

def display_categories(request):
    return render(request, 'categories.html')

def display_StoryList(request):
    return render(request, 'story-list.html')

def display_howToPlay(request):
    return render(request, 'how-to-play.html')

def display_story(request):
    return render(request, 'story.html')

@csrf_exempt
def get_storyList(request):
    print("get_storyList was called")
    storyList = Controller.getStoryList()
    return HttpResponse(storyList, content_type='application/json')

@csrf_exempt
def set_story(request):
    global StoryObject
    pk = request.POST.get("id","")
    print(pk)
    pkAsInt = int(pk)
    StoryObject = Story.Story(pkAsInt + 1)
    return HttpResponse("Set story was called", content_type='text/plain')

@csrf_exempt
def get_story(request):
    story = StoryObject.getStoryArray()
    return HttpResponse(story, content_type='text/plain')

@csrf_exempt
def send_input(request):

    StoryObject.injectWords(request.POST.get("UserInput", ""))
    return HttpResponse("Return was called", content_type='text/plain')

def display_ShowStory(request):

    storyInfo = StoryObject.parseStoryText()

    return HttpResponse(storyInfo, content_type='text/plain')
