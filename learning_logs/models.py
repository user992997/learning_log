from django.db import models

# Create your models here.

class Topic(models.Model):
    text = models.CharField(max_length=200)  #definiendo el campo text
    date_added = models.DateTimeField(auto_now_add=True) #definiendo el campo date_added
    
    def __str__(self):
        return self.text  #retorna text como un string 