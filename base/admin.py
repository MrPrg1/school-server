from django.contrib import admin
from .models import SchoolInfo, ClassInfo, Student, StudentClass



@admin.register(SchoolInfo)
class SchoolInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'educationalStage', 'phoneNumber', 'address', 'typeSchool', 'classNumber', 'studentNumber', 'yearOfCreation', 'control']


@admin.register(ClassInfo)
class ClassInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'studentNumber', 'grade', 'classNumber']




@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'lastName', 'nationalCode', 'phoneNumber', 'fatherPhoneNumber', 'fatherName', 'homePhoneNumber', 'dateOfBirth', 'address', 'image']



@admin.register(StudentClass)
class StudentClassAdmin(admin.ModelAdmin):
    list_display = ['student', 'clas']