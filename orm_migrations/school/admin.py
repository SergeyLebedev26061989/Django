from django.contrib import admin

from .models import Students, Teachers


@admin.register(Students)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    # list_filter = ['category']

@admin.register(Teachers)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
