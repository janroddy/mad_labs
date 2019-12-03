import unittest
import json
from .models import Story
from django.core import serializers

class Controller:

    StoryList = None
    StoryList_JSON = '{}'

    def __init__(self):
        global StoryList
        StoryList = serializers.serialize('json', Story.objects.all(), fields='story_name')
        print(StoryList)
        StoryList = json.dumps(StoryList)
        print(StoryList)

    def getStoryList(self):

        return StoryList
