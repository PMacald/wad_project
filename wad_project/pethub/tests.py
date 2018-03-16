# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import UserProfile, Post, Comment
from django.core.urlresolvers import reverse
from django.conf.urls import url

class PetHubTests(TestCase):
    
    #View Tests
    def test_cant_see_index_while_not_logged_in(self):
        response = self.client.get(reverse('index'))
        self.assertRedirects(response, '/pethub/login/?next=/pethub/index/')
        
    def test_cant_see_about_while_not_logged_in(self):
        response = self.client.get(reverse('about-us'))
        self.assertRedirects(response, '/pethub/login/?next=/pethub/about-us/')

    def test_cant_see_trending_while_not_logged_in(self):
        response = self.client.get(reverse('trending'))
        self.assertRedirects(response, '/pethub/login/?next=/pethub/trending/')

    def test_cant_see_extra_info_while_not_logged_in(self):
        response = self.client.get(reverse('extra-information'))
        self.assertRedirects(response, '/pethub/login/?next=/pethub/extra-information/')

    def test_cant_see_species_while_not_logged_in(self):
        response = self.client.get(reverse('species'))
        self.assertRedirects(response, '/pethub/login/?next=/pethub/species/')

    def test_cant_see_user_profile_while_not_logged_in(self):
        response = self.client.get(reverse('user_profile'))
        self.assertRedirects(response, '/pethub/login/?next=/pethub/user/')

    def test_cant_see_post_upload_while_not_logged_in(self):
        response = self.client.get(reverse('post-upload'))
        self.assertRedirects(response, '/pethub/login/?next=/pethub/post-upload/')

    def test_cant_see_user_logout_while_not_logged_in(self):
        response = self.client.get(reverse('logout'))
        self.assertRedirects(response, '/pethub/login/?next=/pethub/logout/')

    def test_cant_see_update_user_while_not_logged_in(self):
        response = self.client.get(reverse('update-user'))
        self.assertRedirects(response, '/pethub/login/?next=/pethub/update-user/')

    
    
