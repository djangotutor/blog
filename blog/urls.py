from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.Home.as_view(), name='home'),
	url(r'^(?P<category>[ㄱ-ㅣ가-힣|a-zA-Z0-9]+)/$', views.PostList.as_view(), name='posts_by_category'),
	url(r'^post/(?P<pk>\d+)/$', views.PostDetail.as_view(), name='post_detail'),
	url(r'^post/new/$', views.PostNew.as_view(), name='post_new'),
]
