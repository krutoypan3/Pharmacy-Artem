from django.db import models


class Articles(models.Model):
    title = models.CharField(max_length=120)
    text = models.TextField()
    body = models.TextField()
    price = models.CharField(max_length=30)


def __str__(self):
    return self.title
