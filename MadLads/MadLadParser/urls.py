from . import views
from django.conf.urls import url

urlpatterns = [

    url(r'^$', views.display_home, name='display_home'),
    url(r'^home/$', views.display_home, name='display_home'),
    url(r'^about/$', views.display_about, name='display_about'),
    url(r'^categories/$', views.display_categories, name='display_categories'),
    url(r'^how-to-play/$', views.display_howToPlay, name='display_how-to-paly'),
    url(r'^story/$', views.display_story, name='display_story'),
    url(r'^get/$', views.get_story, name='get_story'),
    url(r'^send/$', views.send_input, name='send_input'),
    url(r'^show/$', views.display_ShowStory, name='display_ShowStory'),
]
