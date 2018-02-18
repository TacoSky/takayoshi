from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^qualities/$', views.qualities, name='qualities'),
    url(r'^education/$', views.education, name='education'),
    url(r'^experiences/$', views.experiences, name='experiences'),
    url(r'^portfolio/$', views.portfolio, name='portfolio'),
]



