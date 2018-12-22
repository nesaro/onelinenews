from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.headlines),
    url(r'get/$', views.headline),
]
