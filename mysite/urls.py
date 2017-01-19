from django.conf.urls import include, url

from talkapp import views

urlpatterns = [
    url(r'^$', views.home, name='home'),

    url(r'^users/create/$', views.user_create, name='user_create'),
    url(r'^users/store/$', views.user_store, name='user_store'),
    url(r'^users/edit/$', views.user_edit, name='user_edit'),
    url(r'^users/update/$', views.user_update, name='user_update'),

    url(r'^posts/$', views.post_index, name='post_index'),
    url(r'^posts/create/$', views.post_create, name='post_create'),
    url(r'^posts/store/$', views.post_store, name='post_store'),
    url(r'^posts/delete_all$', views.post_delete_all, name='post_delete_all'),

    url(r'^getlogin/$', views.getLogin, name='getlogin'),
    url(r'^postlogin/$', views.postLogin, name='postlogin'),
    url(r'^getlogout/$', views.getLogout, name='getlogout'),
]
