# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from .models import UserProfile, Post, Comment
from django.core.urlresolvers import reverse
from django.conf.urls import url
import datetime
from django.utils import timezone

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

    #Model Tests
    def test_ensure_2_post_with_same_title_can_exist(self):
        test_post1 = Post(title="Test")
        test_post2 = Post(title="Test")
        self.assertEqual(test_post1==test_post2, False)

    def test_post_cannot_have_negative_likes(self):
        test_post = Post(likes=-1)
        self.assertEqual((test_post.likes >= 0), True) #Currently this test fails, need to edit code elsewhere

    def test_can_have_post_with_historic_date(self):
        time = timezone.now() - datetime.timedelta(days=4)
        test_post = Post(upload_date = time)
        self.assertEqual((test_post.upload_date==timezone.now()), False)

    def test_can_have_2_comments_with_same_text_on_post(self):
        test_comment1 = Comment(comment_text = "Test")
        test_comment2 = Comment(comment_text = "Test")
        self.assertEqual(test_comment1==testcomment2, False)
