from django.urls import path
from webapp.views import create_task, index, task_detail


urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>/', task_detail, name='task_detail'),
    path('create/', create_task, name='create_task'),
]


