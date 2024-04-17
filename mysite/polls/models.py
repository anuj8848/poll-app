from django.db import models

# Create your models here.

class Question(models.Model):
    question_text=models.CharField(max_length=300)
    pub_data=models.DateTimeField("data published")
    

class Choice(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=100)
    votes=models.IntegerField(default=0)
    
    