from django.contrib import admin
from .models import Task

# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'title',
        'description',
        'user',
        'created',
        'modified'
        
    )
    
    readonly_fields = ('created',)
    list_filter = ['title']
    search_fields = ['title', 'description']
