from . import views
from django.conf.urls import url

urlpatterns = [

    url(r'^$', views.display_home, name='display_home'),
    url(r'^home/$', views.display_home, name='display_home'),
    url(r'^about/$', views.display_about, name='display_about'),
     url(r'^help/$', views.display_help, name='display_help'),
    url(r'^categories/$', views.display_categories, name='display_categories'),
    url(r'^how-to-play/$', views.display_howToPlay, name='display_how-to-paly'),
    url(r'^story/$', views.display_story, name='display_story'),
    url(r'^get/$', views.get_story, name='get_story'),
    url(r'^send/$', views.send_input, name='send_input'),
    url(r'^show/$', views.display_ShowStory, name='display_ShowStory'),

    url(r'^set/$', views.set_story, name='set_story'),
    url(r'^get/story-list/$', views.get_storyList, name='get_storyList'),

    url(r'^StoryList-Classics/$', views.display_StoryList_Classics, name='display_StoryList_Classics'),
    url(r'^StoryList-by-Sean/$', views.display_StoryList_by_Sean, name='display_StoryList_by_Sean'),
    url(r'^StoryList-All-Titles/$', views.display_StoryList_All_Titles, name='display_StoryList_All_Titles'),
    url(r'^StoryList-Random/$', views.display_StoryList_Random, name='display_StoryList_Random'),
]
