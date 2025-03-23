from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio/', blank=True)
    link = models.URLField(blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title