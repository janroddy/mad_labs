import random as rand
from .models import Story

class Controller:

    thisStory = None
    pk = None
    Story_text = None

    def __init__(self,PK):

        global thisStory
        global pk
        global Story_text

        pk = PK
        thisStory = Story.objects.get(pk=pk)
        Story_text = thisStory.story_text

    def getStoryArray(self):
        if(pk == -1):
            print("Feature coming soon. Please give a PK for the story you want")

        return thisStory.story_array

    def parseStoryText(self):
        if(pk == -1):
            print("Feature coming soon. Please give a PK for the story you want")

        storyInfo = thisStory.story_name + "," + Story_text
        return storyInfo

    def injectWords(userInput):
        global Story_text
        storyIndex = 0
        inputIndex = 0

        splitStory = thisStory.story_text.split('$')
        for token in splitStory:
            if (token == thisStory.story_array[inputIndex]):
                splitStory[storyIndex] = userInput[inputIndex]
                inputIndex = inputIndex + 1
            storyIndex = storyIndex + 1
        finalStory = splitStory.join('')

        Story_text = finalStory
        return finalStory

    def getPK(self):
        return pk

    def setPK(PK):
        global pk
        pk = PK
        return
