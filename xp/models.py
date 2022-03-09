from ssl import create_default_context
from statistics import mode
from django.db import models
from django.contrib.auth.models import User


STATUS = (
    (0, "Draft"),
    (1, "Publish"),
)

class Xp(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=300, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    hero_image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    sort_override = models.IntegerField(default=99)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    class Meta:
        verbose_name_plural = "Xp"
        ordering = ['sort_override', '-created_at']
    
    def __str__(self):
        return self.title

    
