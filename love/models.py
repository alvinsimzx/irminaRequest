from pyexpat import model
from django.db import models

# Create your models here.
class Answer(models.Model):
    answer = models.BooleanField()

    def __str__(self):
        if(self.answer == True):
            return "Yes"
        elif(self.answer == False):
            return "No"
        else:
            return "None"