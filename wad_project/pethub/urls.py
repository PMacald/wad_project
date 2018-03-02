#Handles urls passed to the pethub app
from django.conf.urls import url
from pethub import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='index'),
    url(r'^about-us/$',views.about_us,name='about-us'),
]
