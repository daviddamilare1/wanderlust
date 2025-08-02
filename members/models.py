from django.db import models
from django.contrib.auth.models import  User
import uuid
from ckeditor.fields import RichTextField






class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email =  models.EmailField()
    username = models.CharField(max_length=200)
    occupation = models.CharField(max_length=50)
    user_picture =  models.ImageField(upload_to='img', blank=False, null=False)
    about_user = models.TextField(max_length=500)
    profile_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True,primary_key=True)
    




    def __str__(self):
        return self.username


