import unittest
import json
import random
from .models import Story
from django.core import serializers

class Controller:

    StoryList = None
    StoryList_JSON = '{}'

    def __init__(self,type=None):
        global StoryList

        if(type == None):
            StoryList = serializers.serialize('json', Story.objects.all(), fields='story_name')
            print(StoryList)
            StoryList = json.dumps(StoryList)
            print(StoryList)

        elif(type == 'Random'):

            StoryList = Story.objects.all()
            print(StoryList)
            rand = (random.randrange(len(StoryList)))
            StoryList = serializers.serialize('json', Story.objects.filter(pk__startswith = StoryList[rand].pk), fields='story_name')
            print(StoryList)
            StoryList = json.dumps(StoryList)

        else:
            StoryList = serializers.serialize('json', Story.objects.filter(story_category__startswith=type))
            print(StoryList)
            StoryList = json.dumps(StoryList)
            print(StoryList)

    def getStoryList(self):

        return StoryList
