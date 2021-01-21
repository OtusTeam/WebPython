from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ToDoItem(models.Model):
    title = models.CharField(max_length=200)
    done = models.BooleanField(default=False, null=False)

    author = models.ForeignKey(Author, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.title} [{'V' if self.done else 'X'}]"


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
