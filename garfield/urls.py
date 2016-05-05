from django.conf.urls import url

from gman.views import home

urlpatterns = [
    url(r'^$', home, name='home'),
]
