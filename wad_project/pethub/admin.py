# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# import db models
from pethub.models import Post, UserProfile, Comment


from django.contrib import admin

# Register your models here.
admin.site.register(Post)
admin.site.register(UserProfile)
admin.site.register(Comment)
