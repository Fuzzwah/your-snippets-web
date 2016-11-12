from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views as token_views
from your_snippets.api import views


urlpatterns = [
    url(r'^$', views.snippet_list),
    url(r'^auth/$', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
    url(r'^add/$', views.snippet_add),
    url(r'^add/images/$', views.images_add),
    url(r'^snippet/(?P<pk>[0-9]+)/$', views.snippet_detail),
    url(r'^token/', token_views.obtain_auth_token),
]

urlpatterns = format_suffix_patterns(urlpatterns)
