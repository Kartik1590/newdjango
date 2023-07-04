from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Posts(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    date_posted=models.DateTimeField(default=timezone.now)
    content=models.TextField()  

    # def __init__(self,author,title,date_posted,content):
    #     self.author=author
    #     self.title=title
    #     self.date_posted=date_posted
    #     self.content=content

    def get_absolute_url(self):
        return reverse('blog-detail',kwargs={'pk':self.pk})
