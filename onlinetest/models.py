# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Admin(models.Model):
    username = models.CharField(max_length=20)
    pwd = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    mail = models.CharField(max_length=20)