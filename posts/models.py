from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length= 75)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateField(auto_now_add= True)

    def __str__(self):
        return self.title
    
#new models for Blogpost  
    
class Author(models.Model):
    name= models.CharField(max_length=255)


class Blog_post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)