from django.db import models
from django.conf import settings

# Create your models here.


class Note(models.Model):
    sentence = models.TextField()
    translation = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sentence

    def shuffle(self):
        return self.objects.all().order_by('?')[5]

class Review(models.Model):
    note = models.ForeignKey(Note)
    commenter = models.ForeignKey(settings.AUTH_USER_MODEL)
    comment = models.TextField()
    photo = models.FileField(blank = True, null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)