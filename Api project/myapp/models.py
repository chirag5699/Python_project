from django.db import models

# Create your models here.

class Employee(models.Model):
    fname=models.CharField(max_length=50)
    email=models.EmailField(unique=True)




    def __str__(self):
      return self.name