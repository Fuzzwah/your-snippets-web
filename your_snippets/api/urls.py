from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views as token_views
from your_snippets.api import views


urlpatterns = format_suffix_patterns([
    url(r'^list/$', views.snippet_list, name='snippet-list'),
    url(r'^auth/$', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls, name='api-admin'),
    url(r'^add/$', views.snippet_add, name='add-snippet'),
    url(r'^images/$', views.images_add, name='add-image'),
    url(r'^snippet/(?P<pk>[0-9]+)/$', views.snippet_detail, name='snippet-detail'),
    url(r'^token/$', token_views.obtain_auth_token, name='api-token'),
])

