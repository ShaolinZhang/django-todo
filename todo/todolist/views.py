from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.models import User
from django.http import Http404
from todolist.models import Todo


def todolist(request):
    todolist = Todo.objects.filter(todoStatus=1)
    finishtodos = Todo.objects.filter(todoStatus=0)
    return render(request, 'todolist/index.html', {'todolist': todolist,'finishtodos': finishtodos})


def finishTodo(request, id=''):
    todo = Todo.objects.get(id=id)
    if todo.todoStatus == 1:
        todo.todoStatus = 0
        todo.save()
        return HttpResponseRedirect('/')
    todolist = Todo.objects.filter(todoStatus=1)
    return render(request, 'todolist/index.html',
                           {'todolist': todolist})


def rollbackTodo(request, id=''):
    todo = Todo.objects.get(id=id)
    if todo.todoStatus == 0:
        todo.todoStatus = 1
        todo.save()
        return HttpResponseRedirect('/')
    todolist = Todo.objects.filter(todoStatus=1)
    return render(request, 'todolist/index.html', {'todolist': todolist})


def deleteTodo(request, id=''):
    try:
        todo = Todo.objects.get(id=id)
    except Exception:
        raise Http404
    if todo:
        todo.delete()
        return HttpResponseRedirect('/')
    todolist = Todo.objects.filter(todoStatus=1)
    return render(reqeust, 'todolist/index.html', {'todolist': todolist})


def addTodo(request):
    if request.method == 'POST':
        newTodo = request.POST['todo']
        priority = request.POST['priority']
        user = User.objects.get(id='1')
        todo = Todo(pubUser=user, todo=newTodo, todoPriority=priority, todoStatus=1)
        todo.save()
        todolist = Todo.objects.filter(todoStatus=1)
        finishtodos = Todo.objects.filter(todoStatus=0)
        return render(request, 'todolist/reloadTodo.html',
                              {'todolist': todolist,
                               'finishtodos': finishtodos})
    else:
        todolist = Todo.objects.filter(todoStatus=1)
        finishtodos = Todo.objects.filter(todoStatus=0)
        return render(request, 'todolist/index.html',
                              {'todolist': todolist,
                               'finishtodos': finishtodos})

def updateTodo(request, id=''):
    if request.method == 'POST':
        try:
            todo = Todo.objects.get(id=id)
        except Exception:
            return HttpResponseRedirect('/')
        newTodo = request.POST['todo']
        priority = request.POST['priority']
        todo.todo = newTodo
        todo.todoPriority = priority
        todo.save()
        todolist = Todo.objects.filter(todoStatus=1)
        finishtodos = Todo.objects.filter(todoStatus=0)
        return HttpResponseRedirect('/')
    else:
        try:
            todo = Todo.objects.get(id=id)
        except Exception:
            raise Http404
        return render(request, 'todolist/updatetodo.html', {'todo': todo})
