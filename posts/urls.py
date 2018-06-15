from django.urls import path, re_path
from django.contrib import admin

from .views import (
	post_list,
	post_create,
	post_detail,
	post_update,
	post_delete,
	PostLikeToggle,
	PostLikeAPIToggle,
	)
app_name ='posts'

urlpatterns = [
	re_path(r'^$', post_list, name='list'),
    re_path(r'^create/$', post_create),
    re_path(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
	re_path(r'^(?P<slug>[\w-]+)/like/$', PostLikeToggle.as_view(), name='like-toggle'),
	re_path(r'^api/(?P<slug>[\w-]+)/like/$', PostLikeAPIToggle.as_view(), name='like-api-toggle'),
    re_path(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
    re_path(r'^(?P<slug>[\w-]+)/delete/$', post_delete),
    #re_path(r'^posts/$', "<appname>.views.<function_name>"),
]
