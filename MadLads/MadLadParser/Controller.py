import unittest
import json
import random
import inspect
from .models import Story
from django.core import serializers

class Controller:

    StoryList = None
    StoryList_JSON = '{}'

    def __init__(self,type=None):
        global StoryList

        if(type == None):

            StoryList = serializers.serialize('json', Story.objects.all(), fields='story_name')
            StoryList = json.dumps(StoryList)

        elif(type == 'Random'):

            StoryList = Story.objects.all()
            rand = (random.randrange(len(StoryList)))
            StoryList = serializers.serialize('json', Story.objects.filter(pk__startswith = StoryList[rand].pk), fields='story_name')
            StoryList = json.dumps(StoryList)

        else:

            StoryList = serializers.serialize('json', Story.objects.filter(story_category__startswith=type))
            StoryList = json.dumps(StoryList)

    def getStoryList(self):
        print("-----%s was called-----" % inspect.stack()[0][3])

        return StoryList
