from django import forms 
from .models import Post
from django.contrib.auth.models import User 

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('name', 'profile_pic')

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your name'}),
        }