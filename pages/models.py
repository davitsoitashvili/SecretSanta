from django.db import models
from accounts.models import User
class LetterModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    letter =  models.TextField(max_length=5000)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.author}'s letter"

class SecretSanta(models.Model):
    santa = models.CharField(max_length=200,unique=True)
    player = models.CharField(max_length=200,unique=True)
    text = models.TextField(max_length=5000)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.santa} - > {self.player}"


