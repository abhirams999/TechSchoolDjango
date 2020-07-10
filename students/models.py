from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):


    address=models.TextField()
    contact=models.BigIntegerField()
    fees_paid=models.BooleanField(default=False)
    picture=models.ImageField(default='student1.png',blank=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    



    def __str__(self):
        return self.user.username
