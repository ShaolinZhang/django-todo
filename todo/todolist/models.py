# !/usr/bin/env python
# -*-coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Todo(models.Model):
    todo = models.CharField(max_length=50)
    postTime = models.DateTimeField(auto_now_add=True)
    pubUser = models.ForeignKey(User)
    todoPriority = models.IntegerField()
    todoStatus = models.IntegerField()

    def __unicode__(self):
        return u'%d %s %s' % (self.id, self.todo, self.todoStatus)

    class Meta:
    	ordering = ['todoPriority', 'postTime']
