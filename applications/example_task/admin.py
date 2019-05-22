from django.contrib import admin

from applications.example_task.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    ordering = []
    list_display = (
        'name',
        'status',
    )
    list_filter = ()
    list_select_related = ()
    readonly_fields = ()
    search_fields = []
    inlines = []
