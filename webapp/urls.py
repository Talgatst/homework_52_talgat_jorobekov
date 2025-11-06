from django.urls import path
from webapp.views import task_list, create_task, delete_task

urlpatterns = [
    path('', task_list),
    path('create/', create_task),
    path('delete/<int:task_id>/', delete_task),
]

