from django.db import models

# Create your models here.


class NewsModel5(models.Model):
    title = models.CharField(default = '', max_length = 100)
    body = models.TextField()
    status = models.BooleanField(default = False)

    def __str__(self):
        return self.title