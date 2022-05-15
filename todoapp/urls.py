from django.contrib import admin
from django.urls import path
from todolist.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todolist/', index, name='TodoList'),

]
