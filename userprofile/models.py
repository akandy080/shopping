from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, default= 'ad')
    last_name = models.CharField(max_length=100, default= 'ad')
    pix = models.ImageField(upload_to='Profile', default='avater.jpg')
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=150)
    dob = models.CharField(max_length=150,)
    nationality = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    state = models.CharField(max_length=30)

    def __str__(self):
        return self.user.username

class Register(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, default= 'ad')
    last_name = models.CharField(max_length=100, default= 'ad')
    pix = models.ImageField(upload_to='Profile', default='profile.jpg')
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=150)
    dob = models.CharField(max_length=150,)
    nationality = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    state = models.CharField(max_length=30)

    def __str__(self):
        return self.user.username
    
