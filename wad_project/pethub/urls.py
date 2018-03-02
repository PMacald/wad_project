#Handles urls passed to the pethub app
from django.conf.urls import url
from pethub import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='index'),
    url(r'^about-us/$',views.about_us,name='about-us'),
    url(r'^login/$',views.user_login,name='login'),
    url(r'^logout/$',views.user_logout,name='logout'),
    url(r'^trending/$',views.trending,name='trending'),
    url(r'^species/$',views.species,name='species'),
    url(r'^extra-information/$',views.extra_information,name='extra-information'),
]
