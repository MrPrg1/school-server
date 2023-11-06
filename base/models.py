from django.db import models


CHOICES_EDUCATIONAL_STAGE = [
    (1, 'مقطع بیش دبستانی'),
    (2, "مقطع ابتدایی"),
    (3, "مقطع متوسطه"),
    (4, "مقطع دانشگاهی"),
]

CHOICES_TYPE_SCHOOL = [
    (1, " مدارس دولتی"),
    (2, "مدارس غیرانتفاعی"),
    (3, "مدرسه نمونه دولتی"),
    (4, "مدرسه تیزهوشان"),
    (5, "مدرسه برای ایرانی‌های خارج از کشور"),
    (6, " مدارس هیئت امنایی"),
    (7, "مدارس اقلیت‌های دینی"),
    (8, "مدارس بزرگسالان (شبانه)"),
    (9, "مدارس حرفه‌ای"),
    (10, "مدارس شاهد"),
    (11, "مدارس قرآنی"),
    (12, "مدرسه ورزش"),
    (13, "مدارس هوشمند"),
]
class SchoolInfo(models.Model):
    name = models.CharField(max_length=100, help_text='نام مدرسه')
    educationalStage = models.IntegerField(choices=CHOICES_EDUCATIONAL_STAGE, help_text='مقطع تحصیلی') 
    phoneNumber = models.IntegerField(help_text='شماره تلفن مدرسه را وارد نمایید')
    address = models.CharField(max_length=300, help_text='آدرس مدرسه')
    typeSchool = models.IntegerField(choices=CHOICES_TYPE_SCHOOL, help_text='نوع مدرسه را انتخاب نمایید')
    classNumber = models.IntegerField(help_text='تعداد کلاس های مدرسه را وارد نمایید')
    studentNumber = models.IntegerField(help_text='تعداد دانش اموزان کل مدرسه<<گنجایش مدرسه>>')
    yearOfCreation = models.IntegerField(help_text='سال ایجاد مدرسه را وارد نمایید')
    control = models.BooleanField(default=True)


    def __str__(self):
        return self.name



class ClassInfo(models.Model):
    name = models.CharField(max_length=100)
    studentNumber = models.IntegerField(help_text='تعداد دانش اموزان کلاس را وارد نمایید ((گنجایش کلاس))')
    grade = models.CharField(max_length=100, help_text='بایه کلاس را وارد نمایید')
    classNumber = models.IntegerField(help_text='شماره کلاس را وارد نمایید')


