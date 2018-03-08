# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

#Model for user profiles on PetHub
class UserProfile(models.Model):
    #link UserProfile to user
    user = models.OneToOneField(User)

    #extra fields for our purposes
    bio = models.CharField(max_length=300,default="",blank=True)
    userPicture = models.ImageField(upload_to='user_images',blank=True)

    def __str__(self):
        return self.user.username


    #for unicode support of Python 2.x
    def __unicode__(self):
        return self.user.username

class Post(models.Model):
    #Needs unique identifier and tags incorporated
    title = models.CharField(max_length=100, default="")
    likes = models.IntegerField(default=0)
    description = models.CharField(max_length=300,default="")
    picture = models.ImageField(upload_to="post_images",blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)

    ######################################################################
    user_profile = models.ForeignKey("UserProfile", default=0)

    def __str__(self):
        return self.title

    #for unicode support of Python 2.x
    def __unicode__(self):
        return self.title
