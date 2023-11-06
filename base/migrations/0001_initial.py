# Generated by Django 4.2.7 on 2023-11-06 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('studentNumber', models.IntegerField(help_text='تعداد دانش اموزان کلاس را وارد نمایید ((گنجایش کلاس))')),
                ('grade', models.CharField(help_text='بایه کلاس را وارد نمایید', max_length=100)),
                ('classNumber', models.IntegerField(help_text='شماره کلاس را وارد نمایید')),
            ],
        ),
        migrations.CreateModel(
            name='SchoolInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='نام مدرسه', max_length=100)),
                ('educationalStage', models.IntegerField(choices=[(1, 'مقطع بیش دبستانی'), (2, 'مقطع ابتدایی'), (3, 'مقطع متوسطه'), (4, 'مقطع دانشگاهی')], help_text='مقطع تحصیلی')),
                ('phoneNumber', models.IntegerField(help_text='شماره تلفن مدرسه را وارد نمایید')),
                ('address', models.CharField(help_text='آدرس مدرسه', max_length=300)),
                ('typeSchool', models.IntegerField(choices=[(1, ' مدارس دولتی'), (2, 'مدارس غیرانتفاعی'), (3, 'مدرسه نمونه دولتی'), (4, 'مدرسه تیزهوشان'), (5, 'مدرسه برای ایرانی\u200cهای خارج از کشور'), (6, ' مدارس هیئت امنایی'), (7, 'مدارس اقلیت\u200cهای دینی'), (8, 'مدارس بزرگسالان (شبانه)'), (9, 'مدارس حرفه\u200cای'), (10, 'مدارس شاهد'), (11, 'مدارس قرآنی'), (12, 'مدرسه ورزش'), (13, 'مدارس هوشمند')], help_text='نوع مدرسه را انتخاب نمایید')),
                ('classNumber', models.IntegerField(help_text='تعداد کلاس های مدرسه را وارد نمایید')),
                ('studentNumber', models.IntegerField(help_text='تعداد دانش اموزان کل مدرسه<<گنجایش مدرسه>>')),
                ('yearOfCreation', models.IntegerField(help_text='سال ایجاد مدرسه را وارد نمایید')),
                ('control', models.BooleanField(default=True)),
            ],
        ),
    ]
