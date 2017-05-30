"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from todolist import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.todolist, name='todo'),
    url(r'^addtodo/$', views.addTodo, name='add'),
    url(r'^todofinish/(?P<id>\d+)/$', views.finishTodo, name='finish'),
    url(r'^todorollback/(?P<id>\d+)/$', views.rollbackTodo,  name='rollback'),
    url(r'^updatetodo/(?P<id>\d+)/$', views.updateTodo, name='update'),
    url(r'^tododelete/(?P<id>\d+)/$', views.deleteTodo, name='delete'),
]
