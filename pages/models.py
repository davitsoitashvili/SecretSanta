from django.db import models
from accounts.models import User
class LetterModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    letter =  models.TextField(max_length=5000)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.author}'s letter"



