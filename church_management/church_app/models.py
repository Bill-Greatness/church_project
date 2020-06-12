from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# from martor.models import MartorField


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50, blank=False, default='Firstname')
    member_id= models.CharField(unique=True, max_length=10, null=True)
    resident_address = models.CharField(blank=True, default='Not Specified',max_length=100)
    surname = models.CharField(max_length=50, blank=False,default='Surname')
    date_of_birth = models.DateField(auto_now=False,default=timezone.now)
    date_added = models.DateField(auto_now=True)
    region = models.CharField(blank=False,max_length=50,default='Region')
    phone_number = models.CharField(unique=True, max_length=10, null=True)
    image = models.ImageField(default='user_image.png',upload_to='profile_images')
    gender = models.CharField(blank=False,max_length=10, default='Gender')
    wing_name = models.CharField(default='Not Provided',max_length=50)


    def __str__(self):
        return f'Profile of {self.user}'



class Forum(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150,null=False)
    content = models.TextField(null=False)
    image = models.ImageField(default=None,upload_to='post_images')
    date_posted = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.title} by {self.author}'



class Request(models.Model):
    full_name = models.CharField(max_length=150, null=False)
    email = models.EmailField(unique=False, null=True)
    phone =  models.CharField(max_length=10, null=False)
    district = models.CharField(max_length=50, null=False)
    request_title = models.CharField(max_length=150, null=False)
    request_content = models.TextField(null=False)
    date_requested = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.request_title} by {self.full_name} on {self.date_requested}'


