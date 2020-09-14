from django.conf.urls import include, url
from django.urls import path
import core.views
urlpatterns = [
    url(r'^$', core.views.home, name='index'),
    url(r'^home$', core.views.home, name='home'),
    url(r'^home$', core.views.home, name='main'),
    path('', core.views.home, name='home')
]
