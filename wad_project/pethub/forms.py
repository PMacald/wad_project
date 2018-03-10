from django import forms
from django.contrib.auth.models import User
from pethub.models import UserProfile, Post


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('userPicture', 'bio')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'description', 'picture', 'tags')

class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('userPicture', 'bio')

class UpdateUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password')
