from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    name = forms.CharField(max_length=100, label='Your Name',widget=forms.TextInput(attrs={'placeholder': 'Your name'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 5,'placeholder': 'Enter Text'}),label='Message')

    class Meta:
        model = Post
        fields = ('name', 'message')