# Generated by Django 5.0.6 on 2024-06-18 19:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0002_student_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='название')),
                ('description', models.TextField(verbose_name='описание')),
                ('students', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='new_app.student', verbose_name='студенты')),
            ],
            options={
                'verbose_name': 'Предмет',
                'verbose_name_plural': 'Предметы',
            },
        ),
    ]
