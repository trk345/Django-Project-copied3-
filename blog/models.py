from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User #User is a class
from django.urls import reverse
from PIL import Image
from django.shortcuts import get_object_or_404
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
# class Category(models.Model):
#     name = models.CharField(max_length=250)
#
#     def __str__(self):
#         return self.name
#
#     def get_absolute_url(self):
#         return reverse('post-detail', kwargs = {'pk':self.pk})

class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, default = None)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)#an author can have many posts
                                                             #but a post can have only one authusor
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs = {'pk':self.pk})

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)







