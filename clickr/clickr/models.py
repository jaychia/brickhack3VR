from django.db import models

class Professor(models.Model):
    profName = models.CharField(max_length=200, null=False)

class Question(models.Model):
    className = models.CharField(max_length=200, null=False)
    professor = models.ForeignKey('Professor' , on_delete=models.CASCADE)
    text = models.TextField()
    active = models.BooleanField()
    room = models.ForeignKey('Room', related_name="questions")

class Option(models.Model):
    question = models.ForeignKey('Question' , on_delete=models.CASCADE)
    sequence = models.IntegerField()
    text = models.TextField()
    correct = models.BooleanField()
    room = models.ForeignKey('Room', related_name='options')

class Student(models.Model):
    options = models.ManyToManyField(Option)
    name = models.CharField(max_length=200, null=False)
    email = models.CharField(max_length=200, null=False)

class Room(models.Model):
    label = models.TextField(null=False, unique=True)
    name = models.TextField(null=False)