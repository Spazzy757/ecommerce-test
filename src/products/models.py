from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title
