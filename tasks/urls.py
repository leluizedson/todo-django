from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_tasks, name='list_tasks'),
    path('<int:id>', views.ver_task, name='ver_task'),
    path('create/', views.create_task, name='create_task'),
    path('<int:id>/edit', views.edit_task, name='edit_task'),
    path('<int:id>/del', views.delete_task, name='delete_task')
]
