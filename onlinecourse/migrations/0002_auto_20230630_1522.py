# Generated by Django 3.1.3 on 2023-06-30 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enrollment',
            old_name='course',
            new_name='course_id',
        ),
        migrations.RenameField(
            model_name='enrollment',
            old_name='user',
            new_name='user_id',
        ),
        migrations.RenameField(
            model_name='instructor',
            old_name='user',
            new_name='user_id',
        ),
        migrations.RenameField(
            model_name='learner',
            old_name='user',
            new_name='user_id',
        ),
        migrations.RenameField(
            model_name='lesson',
            old_name='course',
            new_name='course_id',
        ),
        migrations.RenameField(
            model_name='submission',
            old_name='enrollment',
            new_name='enrollment_id',
        ),
        migrations.AddField(
            model_name='question',
            name='course_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.course'),
            preserve_default=False,
        ),
    ]
