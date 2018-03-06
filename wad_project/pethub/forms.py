from django import forms
from django.contrib.auth.models import User
from pethub.models import UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('userPicture', 'bio')

class PostForm(forms.modelForm):
    class Meta:
        model = Post
        fields = ('title', 'description', 'picture')
