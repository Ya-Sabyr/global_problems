from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=30, blank=False)
    picture = models.FileField()
    text = models.TextField(blank=False)
    comments = models.ForeignKey('Comment', on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    like = models.IntegerField(default=0)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    
    def get_absolute_url(self):
        return reverse('article', args=[str(self.pk)])


class Comment(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.CharField(max_length=70, blank=False)
    like = models.IntegerField(default=0)