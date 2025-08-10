from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_tasks, name='list_tasks'),
    path('task/<int:id>', views.ver_task, name='ver_task')
]