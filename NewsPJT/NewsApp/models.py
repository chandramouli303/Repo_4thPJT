# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Employee1(models.Model):
    ENo = models.IntegerField()
    EName = models.CharField(max_length=(64))
    ESal = models.IntegerField()
    ELoct = models.CharField(max_length=(64))
class Employee2(models.Model):
    ENo = models.IntegerField()
    EName = models.CharField(max_length=(64))
    ESal = models.IntegerField()
    ELoct = models.CharField(max_length=(64))