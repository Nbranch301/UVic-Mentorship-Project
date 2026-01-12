from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created = models.DateTimeField("date created", auto_now_add=True)
    modified = models.DateTimeField("date updated", auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    def get_text(self) -> str:
        return self.text
    
    def __str__(self) -> str:
        return self.title

