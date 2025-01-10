from django.urls import path
from kanban.tasks import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('add/', views.add_task, name='add_task'),
    path('change_status/<int:task_id>/', views.change_status, name='change_status'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
]