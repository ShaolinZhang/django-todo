# !/usr/bin/python
# -*-coding: utf-8 -*-

from django.contrib import admin
from todolist.models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display= ('pubUser', 'todo', 'todoPriority', 'todoStatus', 'postTime',)
    list_filter = ('postTime',)
    ordering = ('-postTime',)

admin.site.register(Todo, TodoAdmin)
# Register your models here.
