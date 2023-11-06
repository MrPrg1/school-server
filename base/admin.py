from django.contrib import admin
from .models import SchoolInfo, ClassInfo



@admin.register(SchoolInfo)
class SchoolInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'educationalStage', 'phoneNumber', 'address', 'typeSchool', 'classNumber', 'studentNumber', 'yearOfCreation', 'control']


@admin.register(ClassInfo)
class ClassInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'studentNumber', 'grade', 'classNumber']