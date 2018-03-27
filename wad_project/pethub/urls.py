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
    url(r'^cat/$',views.cat,name='cat'),
    url(r'^dog/$',views.dog,name='dog'),
    url(r'^hutch-animal/$',views.hutch_animal,name='hutch'),
    url(r'^exotic-animal/$',views.exotic,name='exotic'),
    url(r'^user/$',
        views.user_profile, name='user_profile'),
    url(r'^user/(?P<username>[\w\-]+)$',
        views.user_profile, name='user_profile'),
    url(r'^extra-information/$',views.extra_information,name='extra-information'),
    url(r'^post-upload/$',views.post_upload,name='post-upload'),
    url(r'^update-user/$',views.update_user,name='update-user'),
    url(r'^like/$', views.like, name = 'like_post'),
    url(r'^search/$', views.search, name = 'search'),
    url(r'^delete_post/(?P<post_id>\d+)/$', views.delete_post, name="delete_post"),
    url(r'^delete_comment/(?P<comment_id>\d+)/$', views.delete_comment, name="delete_comment"),
    url(r'^add-comment/$', views.add_comment, name = 'add_comment'),
    url(r'^add-comment/(?P<post_id>\d+)/$', views.add_comment, name = 'add_comment'),
    url(r'^confirm-user-deletion/$', views.confirm_user_deletion, name = 'confirm_user_deletion'),
    url(r'^confirm-user-deletion/(?P<user_id>\d+)/$', views.confirm_user_deletion, name = 'confirm_user_deletion'),
]
