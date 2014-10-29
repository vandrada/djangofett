from django.conf.urls import patterns, url
from portal import views


urlpatterns = patterns('',
                       url(r'^home/$', views.home, name='home'),
                       url(r'^game/(?P<game_id>\d+)/$',
                           views.game, name='game'),
                       url(r'^vote/(?P<question_id>\d+)/$',
                           views.vote, name='vote'),
                       )
