from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Artical(models.Model):
    name    =models.ForeignKey(User,on_delete=models.CASCADE)
    book    =models.CharField(max_length=122)
    email   =models.EmailField()
    date    =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)