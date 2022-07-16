from django.db import models
from django.contrib import admin
import geocoder
# Create your models here.
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
import datetime
from django.db import models
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.utils.text import slugify

access_token = 'pk.eyJ1IjoiZ2F2aW4tZ3VvIiwiYSI6ImNrdm9iZXozaGN3MXoycHQ5am5vOTIzajMifQ.gycEz65lfHwNqvAqZPjQhA'
class Housing(models.Model):
    address = models.CharField(max_length=3000)
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)
    rent = models.IntegerField()
    bed = models.IntegerField()
    bath = models.IntegerField()
    sqft = models.IntegerField()
    image = models.ImageField(upload_to='housing')
    def save(self, *args, **kwargs):
        g = geocoder.mapbox(self.address, key=access_token)
        g = g.latlng
        self.lat = g[0]
        self.long = g[1]
        return super(Housing, self).save(*args, **kwargs)

class Rating(models.Model):
    housing = models.ForeignKey(Housing, on_delete=models.CASCADE)
    rate_text = models.CharField(max_length=200)
    rate = models.IntegerField(default=0)
    #review_text = models.CharField(max_length=300, default='')

class Review(models.Model):
    name = models.CharField(max_length=300, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    housing = models.ForeignKey(Housing, on_delete=models.CASCADE)
    review_text = models.CharField(max_length=300, null=True)

class Profile(models.Model):
    username = models.CharField(max_length=300, null=False, primary_key=True, unique=True, default=" ")
    age = models.CharField(max_length=3, null=True, default=" ")
    gender = models.CharField(max_length=300, null=True, default=" ")
    school_year = models.CharField(max_length=300,null=True,default=" ")
    #USERNAME_FIELD = 'username'
    # @receiver(post_save, sender=User)  # add this
    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Profile.objects.create(user=instance)
    #
    # @receiver(post_save, sender=User)  # add this
    # def save_user_profile(sender, instance, **kwargs):
    #     instance.profile.save()

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(
        default='',
        editable=True,
        max_length=300,
        unique=True
    )
    
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=1)
    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
class AdvicePost(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.title