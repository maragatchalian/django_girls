from django.db import models
from django.utils import timezone

# Create your models here.

#Model
class Post(models.Model):
    author = models.ForeignKey('auth.User')  #properties
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):  #methods
        self.published_date = timezone.now()
        save.save()

    def __str__(self):
        return self.title