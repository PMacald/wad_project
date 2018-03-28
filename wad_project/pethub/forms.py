from django import forms
from django.contrib.auth.models import User
from pethub.models import UserProfile, Post, Comment


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password')

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("The passwords do not match")

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

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_text',)
