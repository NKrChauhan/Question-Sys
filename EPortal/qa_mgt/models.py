from typing import AnyStr
from django.core.exceptions import SuspiciousOperation
from django.db import models
from django.contrib.auth import get_user_model
import datetime

# Create your models here.

User = get_user_model()

answer_choice = [
    ('Option 1','option1'),
    ('Option 2','option2'),
    ('Option 3','option3'),
    ('Option 4','option4'),
]

class QuestionPaper(models.Model):
    time        = models.TimeField(default=datetime.time(0, 30, 00))
    setter      = models.ForeignKey(User,on_delete=models.CASCADE)
    no_of_ques  = models.PositiveIntegerField(default=5,null=False,blank=False)

    def __str__(self):
        return f"{self.setter.username} has set for time: {self.time} => id = {self.id} and {self.no_of_ques} number of questions"

class QuestionBank(models.Model):
    q_paper     = models.ForeignKey(to=QuestionPaper,on_delete=models.CASCADE)
    question    = models.CharField(max_length=500,blank=False,null=False)
    option1     = models.CharField(max_length=50,blank=False,null=False)
    option2     = models.CharField(max_length=50,blank=False,null=False)
    option3     = models.CharField(max_length=50,blank=False,null=False)
    option4     = models.CharField(max_length=50,blank=False,null=False)
    answer      = models.CharField(max_length = 10,choices=answer_choice,null=False,blank=False)
    score       = models.IntegerField(blank=False,null=False)

    def __str__(self):
        return f"{self.q_paper.id}: {self.question}"

class ResposeBank(models.Model):
    answered_by = models.ForeignKey(User,on_delete=models.CASCADE)
    question    = models.ForeignKey(QuestionBank,on_delete=models.CASCADE)
    answer      = models.CharField(max_length = 10,choices=answer_choice,null=False,blank=False)
    score       = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.answered_by} answerd for {self.question.question} => {self.answer}"

class UserScore(models.Model):
    user        = models.ForeignKey(User,on_delete=models.CASCADE)
    q_paper     = models.ForeignKey(to=QuestionPaper,on_delete=models.CASCADE)
    timestamp   = models.DateTimeField(auto_now=True)
    total_score = models.IntegerField(default=0) 

    def __str__(self):
        return f"{self.user} got {self.total_score} for {self.q_paper.id}"
