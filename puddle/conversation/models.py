from django.db import models
from item.models import Item
from django.contrib.auth.models import User

class Conversation(models.Model):
    item = models.ForeignKey(Item,related_name="conversations",on_delete=models.CASCADE)
    member = models.ForeignKey(User,related_name="conversations",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-updated_at',)

class ConversationMessage(models.Model):
    conversation = models.ForeignKey(Conversation,related_name="message",on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,related_name="message",on_delete=models.CASCADE)