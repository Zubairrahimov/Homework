from django.db import models

# Create your models here.

class User9(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    second_name = models.CharField(max_length=100)
    job = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    