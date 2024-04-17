# Generated by Django 5.0.4 on 2024-04-16 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0006_faculty_remove_student_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher', models.CharField(max_length=100)),
                ('clarity', models.IntegerField()),
                ('engagement', models.IntegerField()),
                ('approachability', models.IntegerField()),
                ('management', models.IntegerField()),
                ('fairness', models.IntegerField()),
                ('feedback', models.IntegerField()),
                ('encouragement', models.IntegerField()),
                ('organization', models.IntegerField()),
                ('teaching', models.IntegerField()),
                ('satisfaction', models.IntegerField()),
            ],
        ),
    ]
