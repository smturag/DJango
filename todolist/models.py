from django.db import models

class user_info(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()

