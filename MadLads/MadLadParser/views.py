from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from MadLadParser import Story
from MadLadParser import Controller

import inspect

StoryObject = None
controller = None

# Create your views here.
def display_home(request):
    print("-----%s was called-----" % inspect.stack()[0][3])
    return render(request, 'index.html')

def display_about(request):
    print("-----%s was called-----" % inspect.stack()[0][3])
    return render(request, 'about.html')

def display_categories(request):
    print("-----%s was called-----" % inspect.stack()[0][3])
    return render(request, 'categories.html')
def display_help(request):
    print("-----%s was called-----" % inspect.stack()[0][3])
    return render(request, 'help.html')

#SPECIFIC CATEGORY OF STORIES
def display_StoryList_Classics(request):
    print("-----%s was called-----" % inspect.stack()[0][3])
    global controller
    controller = Controller.Controller('Classics')
    return render(request, 'story-list.html')

def display_StoryList_by_Sean(request):
    print("-----%s was called-----" % inspect.stack()[0][3])
    global controller
    controller = Controller.Controller('by Sean')
    return render(request, 'story-list.html')

def display_StoryList_All_Titles(request):
    print("-----%s was called-----" % inspect.stack()[0][3])
    global controller
    controller = Controller.Controller()
    return render(request, 'story-list.html')

def display_StoryList_Random(request):
    print("-----%s was called-----" % inspect.stack()[0][3])
    global controller
    controller = Controller.Controller('Random')
    return render(request, 'story.html')

#END SPECIFIC CATEGORIES

def display_howToPlay(request):
    print("-----%s was called-----" % inspect.stack()[0][3])
    return render(request, 'how-to-play.html')

def display_story(request):
    print("-----%s was called-----" % inspect.stack()[0][3])
    return render(request, 'story.html')

@csrf_exempt
def get_storyList(request):
    print("-----%s was called-----" % inspect.stack()[0][3])
    storyList = controller.getStoryList()
    return HttpResponse(storyList, content_type='application/json')

@csrf_exempt
def set_story(request):
    print("-----%s was called-----" % inspect.stack()[0][3])
    global StoryObject
    pk = request.POST.get("id","")
    pkAsInt = int(pk)
    StoryObject = Story.Story(pkAsInt)
    return HttpResponse("Set story was called", content_type='text/plain')

@csrf_exempt
def get_story(request):
    print("-----%s was called-----" % inspect.stack()[0][3])
    story = StoryObject.getStoryArray()
    return HttpResponse(story, content_type='text/plain')

@csrf_exempt
def send_input(request):
    print("-----%s was called-----" % inspect.stack()[0][3])

    StoryObject.injectWords(request.POST.get("UserInput", ""))
    return HttpResponse("Return was called", content_type='text/plain')

def display_ShowStory(request):
    print("-----%s was called-----" % inspect.stack()[0][3])

    storyInfo = StoryObject.parseStoryText()

    return HttpResponse(storyInfo, content_type='text/plain')
