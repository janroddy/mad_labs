import random as rand
from .models import Story as StoryTable

class Story:

    thisStory = None
    pk = None
    Story_text = None

    def __init__(self,PK):

        global thisStory
        global pk

        pk = PK
        thisStory = StoryTable.objects.get(pk=pk)

    def getStoryArray(self):
        if(pk == -1):
            print("Feature coming soon. Please give a PK for the story you want")

        return thisStory.story_array

    def parseStoryText(self):
        if(pk == -1):
            print("Feature coming soon. Please give a PK for the story you want")

        storyInfo = thisStory.story_name + "^" + Story_text
        return storyInfo

    def injectWords(self,userInput):

        global Story_text
        storyIndex = 0
        inputIndex = 0

        splitStory = thisStory.story_text.split('$')
        storyArray = thisStory.story_array.split(',')
        userInput = userInput.split(',')

        print("#########################################")
        print(splitStory)
        print(storyArray)
        print(userInput)
        print("#########################################")

        for token in splitStory:
            print("TOKEN: " + token)
            if (token == storyArray[inputIndex]):
                print(storyArray[inputIndex])
                print(inputIndex)
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
        return pk

    def setPK(PK):
        global pk
        pk = PK
        return
