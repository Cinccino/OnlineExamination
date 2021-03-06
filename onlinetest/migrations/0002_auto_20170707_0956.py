# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-07 01:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlinetest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paper_Content',
            fields=[
                ('paperquestionid', models.AutoField(primary_key=True, serialize=False)),
                ('answer', models.CharField(max_length=20, null=True)),
                ('score', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PaperInfo',
            fields=[
                ('paperid', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionBank',
            fields=[
                ('questionid', models.AutoField(primary_key=True, serialize=False)),
                ('chioce', models.CharField(max_length=100, null=True)),
                ('content', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=100)),
                ('score', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Studnet',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, unique=True)),
                ('pwd', models.CharField(max_length=20)),
                ('mail', models.EmailField(max_length=20)),
                ('major', models.CharField(max_length=20)),
                ('grade', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'student',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('subjectid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'verbose_name': 'subject',
            },
        ),
        migrations.CreateModel(
            name='Subject_Teacher',
            fields=[
                ('teachertosubjectid', models.AutoField(primary_key=True, serialize=False)),
                ('subjectid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ST_Subject', to='onlinetest.Subject')),
            ],
            options={
                'verbose_name': 'STrelate',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, unique=True)),
                ('pwd', models.CharField(max_length=20)),
                ('mail', models.EmailField(max_length=20)),
            ],
            options={
                'verbose_name': 'teacher',
            },
        ),
        migrations.AlterModelOptions(
            name='admin',
            options={'verbose_name': 'admin'},
        ),
        migrations.RemoveField(
            model_name='admin',
            name='id',
        ),
        migrations.AlterField(
            model_name='admin',
            name='mail',
            field=models.EmailField(max_length=20),
        ),
        migrations.AlterField(
            model_name='admin',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='admin',
            name='username',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='subject_teacher',
            name='teachername',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ST_Teacher', to='onlinetest.Teacher'),
        ),
        migrations.AddField(
            model_name='questionbank',
            name='subjectid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CQ_Subject', to='onlinetest.Subject'),
        ),
        migrations.AddField(
            model_name='paperinfo',
            name='studentid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PI_Student', to='onlinetest.Studnet'),
        ),
        migrations.AddField(
            model_name='paperinfo',
            name='subjectid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PI_Subject', to='onlinetest.Subject'),
        ),
        migrations.AddField(
            model_name='paper_content',
            name='paperid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PF_Paper', to='onlinetest.PaperInfo'),
        ),
        migrations.AddField(
            model_name='paper_content',
            name='questionid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PF_Question', to='onlinetest.QuestionBank'),
        ),
    ]
