from django import forms
from django.forms import ModelForm
from .models import *









class PostBlog (ModelForm):
    class Meta:
        model = Post
        exclude =['slug','author', 'likes']







class CommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'forms-control bg-dark text-white', 'rows':3, 'col-sm':6, 'placeholder': 'Say something' }))
    class Meta:
        model = Comment
        fields = ['body']





# class ContactForm(forms.Form):
#      name = forms.CharField(
#         max_length=100,
#         widget=forms.TextInput(attrs={ 'class': 'form-control', 'placeholder':'Your Fullname'})
#     )
     
#      email = forms.EmailField(
#         widget=forms.EmailInput(attrs={'id': 'email', 'class': 'form-control', 'placeholder':'Your Email'})
#     )
     
#      subject = forms.CharField(
#         max_length=100,
#         widget=forms.TextInput(attrs={'id': 'subject', 'class': 'form-control', 'placeholder':'Subject'})
#     )
     
#      message = forms.CharField(
#         widget=forms.Textarea(attrs={'id': 'message', 'class': 'form-control', 'rows': 5, 'placeholder':'Message'})
#     )
    
   