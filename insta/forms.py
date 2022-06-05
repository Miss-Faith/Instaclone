from django import forms
from .models import *
from django.forms import ClearableFileInput

class NewPostForm(forms.ModelForm):
	content = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=True)
	caption = forms.CharField(widget=forms.Textarea(attrs={'class': 'input is-medium'}), required=True)
	tags = forms.CharField(widget=forms.TextInput(attrs={'class': 'input is-medium'}), required=True)

	class Meta:
		model = Post
		fields = ('content', 'caption', 'tags')
    
class CommentForm(forms.ModelForm):
	body = forms.CharField(widget=forms.Textarea(attrs={'class': 'textarea'}), required=True)

	class Meta:
		model = Comment
		fields = ('body',)