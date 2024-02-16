from django import forms
from .models import Comment

class EmailPostForm(forms.Form):
	name = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'placeholder': 'Sender Name', 'style': 'width: 50%;', 'class': 'form-control'}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder' :'Sender Email', 'style': 'width: 50%;', 'class': 'form-control'}))
	to = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder' :'Reciepient Email', 'style': 'width: 50%;', 'class': 'form-control'}))
	comments = forms.CharField(required=False, widget=forms.Textarea(attrs={'placeholder': 'comments or Message', 'style': 'width: 50%;', 'class': 'form-control'}))

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('name', 'email', 'body')