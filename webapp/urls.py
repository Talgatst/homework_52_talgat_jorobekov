from django.urls import path
from webapp.views import create_task, index, task_detail, edit_task, delete_task


urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>/', task_detail, name='task_detail'),
    path('create/', create_task, name='create_task'),
    path('<int:pk>/edit/', edit_task, name='edit_task'),
    path('<int:pk>/delete/', delete_task, name='delete_task'),
]


