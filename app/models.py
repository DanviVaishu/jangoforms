from django.db import models
class School(models.Model):
    Sname=models.CharField(max_length=100,primary_key=True)
    Slocation=models.CharField(max_length=100)
    Sprincipal=models.CharField(max_length=100)
    Email=models.EmailField(default='vaishu@gmail.com')
    ReenterEmail=models.EmailField(default='vaishu@gmail.com')
    def __str__(self):
        return self.Sname
    

