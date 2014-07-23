from django.conf.urls import patterns, url

from vandali import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^portfolio/$', views.portfolio, name='portfolio'),
    url(r'^contact/$', views.blog, name='blog'),
    url(r'^blog/$', views.blog, name='blog'),
)