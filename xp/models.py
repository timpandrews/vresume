from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from taggit.managers import TaggableManager
from taggit.models import Tag

STATUS = (
    (0, "Draft"),
    (1, "Publish"),
)

TAG_TYPES = (
    (0, "Technology"),
    (1, "Skills"),
    (2, "Personal"),
)

class Xp(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=300, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    hero_image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    sort_override = models.IntegerField(default=99)
    tags = TaggableManager()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    class Meta:
        verbose_name_plural = "Xp"
        ordering = ['sort_override', '-created_at']
    
    def __str__(self):
        return self.title


class TagType(models.Model):
    tag = models.OneToOneField(Tag, on_delete=models.CASCADE)
    tag_type = models.IntegerField(choices=TAG_TYPES, default=0)

@receiver(post_save, sender=Tag)
def create_tag_type(sender, instance, created, **kwargs):
    if created:
        print('create')
        TagType.objects.create(tag=instance)

@receiver(post_save, sender=Tag)
def save_tag_type(sender, instance, **kwargs):
    print('save')
    instance.tagtype.save()