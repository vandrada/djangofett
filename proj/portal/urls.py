from django.conf.urls import patterns, url
from portal import views

urlpatterns = patterns('',
    url(r'^$', views.home),
    url(r'^home/$', views.home, name='home'),
    url(r'^game/(?P<game_id>\d+)/$', views.game, name='game'),
    url(r'^vote/(?P<question_id>\d+)/$', views.vote, name='vote'),
    url(r'^review/(?P<review_id>\d+)/$', views.review, name='review'),
    url(r'^platform/(?P<platform_id>\d+)/$', views.game_list, name='game_list'),
    # For User Control
    url(r'^doreg/', views.userctrl_doreg, name='usr_reg'),
    url(r'^login/', views.userctrl_login, name='usr_login'),
    url(r'^logout/', views.userctrl_logout, name='usr_logout'),
)
