from django.db import models
import uuid
from django.conf import settings
from django.contrib.auth.models import  User
from django.utils import timezone
from ckeditor.fields import RichTextField
from members.models import UserProfile

class Post(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True,blank=True)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='img')
    body = RichTextField()
    post_id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    slug = models.SlugField()
    category =models.ForeignKey('Category', on_delete=models.SET_NULL, blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='post')


    def __str__(self):
        return self.title




class Category (models.Model):
    category_title = models.CharField(max_length=100)
    category_id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    slug = models.SlugField()


    def __str__(self):
        return self.category_title
    




class Comment(models.Model):
    blog = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name= 'comments')
    date = models.DateTimeField(default=timezone.now)
    

    def __str__(self):
        return self.body
    







class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()


    def __str__(self):
        return self.name