from django.db import models

class Notes(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


