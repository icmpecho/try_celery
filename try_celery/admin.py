from django.contrib import admin
from djcelery.models import TaskMeta


@admin.register(TaskMeta)
class TaskMetaAdmin(admin.ModelAdmin):
    readonly_fields = ('task_id', 'result', 'status', 'date_done')
    list_display = ('task_id', 'date_done', 'status')
