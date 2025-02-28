from django.contrib import admin

from .models import Task, Accomplishment 

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('description', 'user', 'startdate', 'enddate', 'interval_days')

@admin.register(Accomplishment)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task__description', 'task__user', 'date', 'notes')
