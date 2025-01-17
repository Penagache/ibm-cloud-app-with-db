# Generated by Django 3.1.3 on 2023-06-30 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_auto_20230630_1522'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='question_id',
            new_name='question',
        ),
        migrations.RenameField(
            model_name='enrollment',
            old_name='course_id',
            new_name='course',
        ),
        migrations.RenameField(
            model_name='enrollment',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='instructor',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='learner',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='course_id',
            new_name='course',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='lesson_id',
            new_name='lesson',
        ),
        migrations.RenameField(
            model_name='submission',
            old_name='enrollment_id',
            new_name='enrollment',
        ),
    ]
