# Generated by Django 4.1.5 on 2023-02-01 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_remove_student_teacher_student_teacher'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name_plural': 'Ученики'},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name_plural': 'Учителя'},
        ),
    ]
