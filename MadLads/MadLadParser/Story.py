import random as rand
import inspect
from .models import Story as StoryTable

class Story:

    thisStory = None
    pk = None
    Story_text = None

    def __init__(self,PK):
        print("-----A Story object with pk %d was created-----" % PK)

        global thisStory
        global pk

        pk = PK
        thisStory = StoryTable.objects.get(pk=pk)

    def getStoryArray(self):
        print("-----%s was called-----" % inspect.stack()[0][3])
        if(pk == -1):
            print("Feature coming soon. Please give a PK for the story you want")

        return thisStory.story_array

    def parseStoryText(self):
        print("-----%s was called-----" % inspect.stack()[0][3])
        if(pk == -1):
            print("Feature coming soon. Please give a PK for the story you want")

        storyInfo = thisStory.story_name + "^" + Story_text
        return storyInfo

    def injectWords(self,userInput):

        print("-----%s was called-----" % inspect.stack()[0][3])
        global Story_text
        storyIndex = 0
        inputIndex = 0

        splitStory = thisStory.story_text.split('$')
        storyArray = thisStory.story_array.split(',')
        userInput = userInput.split(',')

        for token in splitStory:

            if (token == storyArray[inputIndex]):

                splitStory[storyIndex] = userInput[inputIndex]
                inputIndex = inputIndex + 1
            storyIndex = storyIndex + 1
            if(inputIndex == len(storyArray)):
                break

        storyIndex = 0
        inputIndex = 0
        finalStory = ""
        finalStory = finalStory.join(splitStory)

        Story_text = finalStory
        return finalStory

    def getPK(self):
        print("-----%s was called-----" % inspect.stack()[0][3])
        return pk

    def setPK(PK):
        print("-----%s was called-----" % inspect.stack()[0][3])
        global pk
        pk = PK
        return
