from django.db import models

# Create your models here.
class StudentModel(models.Model):
    
    stud_name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField()
    phone=models.CharField(max_length=100)    
    