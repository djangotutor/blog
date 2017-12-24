from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.Home.as_view(), name='home'),
	url(r'^[^(drafts)](?P<category>[ㄱ-ㅣ가-힣|a-zA-Z0-9]+)/$', views.PostList.as_view(), name='posts_by_category'),
	url(r'^post/(?P<pk>\d+)/$', views.PostDetail.as_view(), name='post_detail'),
	url(r'^post/new/$', views.PostNew.as_view(), name='post_new'),
	url(r'^post/(?P<pk>\d+)/edit/$', views.PostEdit.as_view(), name='post_edit'),
	url(r'^drafts/$', views.PostDraftList.as_view(), name='post_draft_list'),
	url(r'^post/(?P<pk>\d+)/publish/$', views.PostPublish.as_view(), name='post_publish'),
	url(r'^post/(?P<pk>\d+)/remove/$', views.PostRemove.as_view(), name='post_remove'),
	url(r'^post/(?P<pk>\d+)/comment/$', views.CommentAdd.as_view(), name='add_comment_to_post'),
]
