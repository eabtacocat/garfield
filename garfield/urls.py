from django.conf.urls import url

from garfield import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
]
