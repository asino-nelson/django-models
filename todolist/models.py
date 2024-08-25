from django.db import models
from django.contrib.auth.models import User

from client.models import Client

class Todolist(models.Model):
    client = models.ForeignKey(Client, related_name='todolists', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, related_name='todolists', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)