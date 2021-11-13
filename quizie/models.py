from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Quiz(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
    
    def get_questions(self):
        return self.question_set.all()


class Question(models.Model):
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE,default=1)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    
    def get_answers(self):
        return self.answer_set.all()

class Answer(models.Model):
    title = models.CharField(max_length=100)
    correct = models.BooleanField(default=False)
    questions = models.ForeignKey(Question,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class SaveAns(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE,default=1)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    selopt = models.CharField(max_length=100)
    correct = models.CharField(max_length=100)

    def __str__(self):
        return self.selopt
    
class Result(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE)
    marks = models.CharField(max_length=50)

    def __str__(self):
        return self.quiz.title +" - "+self.user.username
    