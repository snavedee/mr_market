from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)  # For clean URLs

    def __str__(self):
        return self.title