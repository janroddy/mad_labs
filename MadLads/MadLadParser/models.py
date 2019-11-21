from django.db import models

# Create your models here.
class Story(models.Model):

    story_name = models.CharField(max_length = 200)
    story_text = models.CharField(max_length = 1500)

    def __str__(self):
        return self.story_name
