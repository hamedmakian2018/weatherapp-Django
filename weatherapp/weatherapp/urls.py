from django.conf.urls import include, url
import core.views


# Django processes URL patterns in the order they appear in the array
urlpatterns = [
    url(r'^$', core.views.home, name='index'),
    url(r'^home$', core.views.home, name='home'),
    url(r'^home$', core.views.home, name='main'),
]
