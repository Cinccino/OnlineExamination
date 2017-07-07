# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
# person = models.ForeignKey(Person, related_name='person_book')  
class Admin(models.Model):
    username = models.CharField(max_length=20,primary_key=True)
    name = models.CharField(max_length=20,unique=True)
    pwd = models.CharField(max_length=20)
    mail = models.EmailField(max_length=20)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name=('admin')
    # 二名

class Studnet(models.Model):
    username = models.CharField(max_length=20,primary_key=True)
    name = models.CharField(max_length=20,unique=True)
    pwd = models.CharField(max_length=20)
    mail = models.EmailField(max_length=20)
    major = models.CharField(max_length=20)
    grade = models.CharField(max_length=20)
    class Meta:
        verbose_name=('student')

class Teacher(models.Model):
    username = models.CharField(max_length=20,primary_key=True)
    name = models.CharField(max_length=20,unique=True)
    pwd = models.CharField(max_length=20)
    mail = models.EmailField(max_length=20)
    class Meta:
        verbose_name=('teacher')

class Subject(models.Model):
    subjectid = models.CharField(max_length=20,primary_key=True)
    name = models.CharField(max_length=20,unique=True)
    class Meta:
        verbose_name=('subject')

class Subject_Teacher(models.Model):
    teachertosubjectid = models.AutoField(primary_key=True)
    teachername = models.ForeignKey(Teacher, related_name='ST_Teacher') 
    subjectid = models.ForeignKey(Subject, related_name='ST_Subject')
    class Meta:
        verbose_name=('STrelate')


# class ChoiceQuestion(models.Model):
#     choicequestionid = models.AutoField(max_length=20,primary_key=True)
#     subjectid = models.ForeignKey(Subject, related_name='CQ_Subject')
#     chioce = models.CharField(max_length=100,unique=True)
#     content = models.CharField(max_length=100)
#     answer = models.CharField(max_length=100)
#     score = models.CharField(max_length=20)

# class SubjectiveQuestion(models.Model):
#     subjectivequestionid = models.AutoField(max_length=20,primary_key=True)
#     subjectid = models.ForeignKey(Subject, related_name='SQ_Subject')
#     content = models.CharField(max_length=200)
#     answer = models.CharField(max_length=200)
#     score = models.CharField(max_length=20)

class QuestionBank(models.Model):
    questionid = models.AutoField(primary_key=True)
    subjectid = models.ForeignKey(Subject, related_name='CQ_Subject')
    chioce = models.CharField(max_length=100,null=True)
    content = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    score = models.CharField(max_length=20)
    # concering add flag to figure subjective
    class Meta:
        verbose_name=('questionbank')


class PaperInfo(models.Model):
    paperid = models.AutoField(primary_key=True)
    subjectid = models.ForeignKey(Subject, related_name='PI_Subject')
    studentid = models.ForeignKey(Studnet, related_name='PI_Student')
    date = models.DateField(max_length=20)
    semester = models.CharField(max_length=20)
    class Meta:
        verbose_name=('paperinfo')

# class Paper_Content(models.Model):
#     paperquestionid = models.AutoField(primary_key=True)
#     paperid = models.ForeignKey(Teacher, related_name='PC_Paper') 
#     questionid = models.ForeignKey(QuestionBank, related_name='PC_Question')


class Paper_Content(models.Model):
    paperquestionid = models.AutoField(primary_key=True)
    paperid = models.ForeignKey(PaperInfo, related_name='PF_Paper')
    questionid = models.ForeignKey(QuestionBank, related_name='PF_Question')
    answer = models.CharField(max_length=20,null=True)
    score = models.CharField(max_length=20,null=True)
    class Meta:
        verbose_name=('papercontent')

class Student_Class(models.Model):
    studenttoclassid = models.AutoField(primary_key=True)
    studentid = models.ForeignKey(Studnet, related_name='SC_Student')
    subjectid = models.ForeignKey(Subject, related_name='SC_Subject')
    semester = models.CharField(max_length=20)