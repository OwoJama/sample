from django.db import models

# Create your models here.


class registration(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    message = models.TextField(max_length=500, default='Welcome')
    image = models.ImageField(upload_to='images/')


class reference(models.Model):
    author = models.ForeignKey(registration, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(default='nil')
