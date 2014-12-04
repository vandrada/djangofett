from django.conf.urls import patterns, url
from portal import views

urlpatterns = patterns('',
    url(r'^$', views.home),
    url(r'^home/$', views.home, name='home'),
    url(r'^game/(?P<game_id>\d+)/$', views.game, name='game'),
    # voting
    url(r'^vote/(?P<question_id>\d+)/(?P<answer_id>\d+)/$',
        views.vote, name='vote'),
    url(r'^result/(?P<question_id>\d+)/$', views.result, name='result'),
    # reviews
    #review_comment is now review. I think review has been superceded,
    #but am leaving the review_comment stuff in comments below just in case.
    url(r'^review/(?P<review_id>\d+)/$', views.review, name='review'),
    url(r'^review/(?P<review_id>\d+)/report/$', views.review_report,
        name='review_report'),
    url(r'^review/(?P<review_id>\d+)/karma/$', views.review_karma,
        name='review_karma'),
    #url(r'^review/(?P<review_id>\d+)/$', views.review_comment,
    #    name='review_comment'),
    url(r'^game/(?P<review_id>\d+)/edit/$', views.review_edit,
        name='review_edit'),
    url(r'^game/(?P<game_id>\d+)/create/$', views.review_create, name='review_create'),
    # Game List/Search
    url(r'^listgames/(?P<platform_id>\w+)/$', views.game_list, name='game_list'),
    # For User Control
    url(r'^userctrl/doreg/', views.userctrl_doreg, name='usr_reg'),
    url(r'^userctrl/login/', views.userctrl_login, name='usr_login'),
    url(r'^userctrl/logout/', views.userctrl_logout, name='usr_logout'),
    url(r'^user/(?P<user_id>\d+)/$', views.user, name='user'),
    url(r'^user/(?P<user_id>\d+)/about/', views.edit_about, name='about'),
)
