from django.contrib import admin
from webapp.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('description', 'status', 'deadline_date')
    list_filter = ('status', 'deadline_date')
    search_fields = ('description',)
