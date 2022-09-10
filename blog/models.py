from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField()
    content = models.CharField(max_length=300)
    published_date = models.DateTimeField(auto_now_add=True)
    
    


    def __str__(self):
        return f"{self.title}"
