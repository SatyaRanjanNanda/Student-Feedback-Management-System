# Generated by Django 5.0.4 on 2024-04-17 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0010_feedback_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin_Dashboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_students', models.IntegerField(default=0)),
                ('total_faculties', models.IntegerField(default=0)),
                ('total_feedback', models.IntegerField(default=0)),
            ],
        ),
    ]