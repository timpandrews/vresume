from django.db import models

class Xp(models.Model):
    placeholder = models.CharField(max_length=25)
    hero_image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    def __str__(self):
        return self.placeholder

    class Meta:
        verbose_name_plural = "Xp"
