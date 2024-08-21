from django.db import models

class Review(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    excerpt = models.TextField()
    image = models.URLField()
    detail_text = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


