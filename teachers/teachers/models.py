from django.db import models
from django.contrib.auth.models import User
    
#
#  Classification
#
class Theme(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
      return self.name

class Chapter(models.Model):
    name = models.CharField(max_length=30)

    theme = models.ForeignKey(Theme, related_name="chapters")

    def __str__(self):
      return self.name

class Student(User):
    lastname = models.CharField(max_length=30)
    firstname = models.CharField(max_length=30)
    done_skills = models.ManyToManyField('Skill')
    
    def __str__(self):
        return '%s %s' % (self.firstname, self.lastname)
        
class Teacher(Student):
    pass

class Exercise(models.Model):
    user = models.ManyToManyField(Student)
    owner = models.ForeignKey(Teacher)
    chapter = models.ManyToManyField(Chapter)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    num_exercise = models.IntegerField()
    level = models.CharField(max_length=60)
    data_type = models.ForeignKey("Exercise_type")
    hints = models.CharField(max_length=50)
    comment = models.CharField(max_length=200)

class Group(models.Model):
    name = models.CharField(max_length=30)
    teacher = models.ManyToManyField(Teacher)
    student = models.ManyToManyField(Student)
    homework = models.ManyToManyField(Exercise)