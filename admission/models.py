

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class NewStudent(models.Model):

    name=models.CharField(max_length=50)
    address=models.TextField()
    contact=models.BigIntegerField()
    email=models.EmailField(max_length=100)
    picture=models.ImageField(default='student1.png',blank=True)
    last_name=models.CharField(max_length=50)


    def __str__(self):
        return self.name
