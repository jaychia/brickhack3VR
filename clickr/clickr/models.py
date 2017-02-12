from django.db import models

class Question(models.Model):
    className = models.CharField(max_length=200, null=False)
    text = models.TextField()
    active = models.BooleanField()

class Option(models.Model):
    question = models.ForeignKey('Question' , on_delete=models.CASCADE)
    sequence = models.IntegerField()
    text = modes.TextField()
    correct = BooleanField()
    students = models.ManytoManyField(Student)

 class Student(models.Model):
    options = models.ManytoManyField(Option)
    name = models.CharField(max_length=200, null=False)
    email = models.CharField(max_length=200, null=False)


