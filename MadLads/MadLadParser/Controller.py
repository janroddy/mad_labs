import random as rand
from .models import Story
def getStoryArray(PK = -1):
    if(PK == -1):
        print("Feature coming soon. Please give a PK for the story you want")

    return Story.objects.get(pk=PK).story_array

def parseStoryText(PK = -1):
    if(PK == -1):
        print("Feature coming soon. Please give a PK for the story you want")

    thisStory  = Story.objects.get(pk=PK)
    storyInfo = thisStory.story_name + "," + thisStory.story_text
    return storyInfo
