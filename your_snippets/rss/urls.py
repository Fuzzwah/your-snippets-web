from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from your_snippets.rss import views


urlpatterns = [
    url(r'^$', views.rss_feed),
]

urlpatterns = format_suffix_patterns(urlpatterns)
