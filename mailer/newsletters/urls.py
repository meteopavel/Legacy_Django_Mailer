from django.conf.urls import url
from .views import create_newsletter, track_open

urlpatterns = [
    url(r'^create-newsletter/$', create_newsletter,
        name='create_newsletter'),
    url(r'^track_open/(?P<newsletter_id>\d+)/(?P<subscriber_id>\d+)/$',
        track_open, name='track_open')
]
