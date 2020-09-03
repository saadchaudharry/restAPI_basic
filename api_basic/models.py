from django.db import models

# Create your models here.


class Artical(models.Model):
    name    =models.CharField(max_length=122)
    book    =models.CharField(max_length=122)
    email   =models.EmailField()
    date    =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)