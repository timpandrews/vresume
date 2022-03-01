from django.db import models

class Resume(models.Model):
    name = models.CharField(max_length=100)
    filename = models.FileField(upload_to='resume/', blank=True)
    def __str__(self):
        return self.name

