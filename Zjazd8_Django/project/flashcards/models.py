from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Flashcard(models.Model):
    name = models.CharField(max_length=100)
    question = models.TextField(max_length=1000)
    answer = models.TextField(max_length=1000)
    slug = models.SlugField(max_length=100, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def learn_url(self):
        return reverse("learn-flashcard", args=[self.slug])


class UserFlashcardRelationship(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flashcard = models.ForeignKey(Flashcard, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} + {self.flashcard.name}"
