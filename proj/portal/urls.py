from django.conf.urls import patterns, url
from portal import views


urlpatterns = patterns('',
                       url(r'^(?P<game_id>\d+)/$', views.game, name='game'),
                       url(r'^home$', views.home, name='home')
                       )
