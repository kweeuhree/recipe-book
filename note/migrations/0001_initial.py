# Generated by Django 5.0.7 on 2024-07-13 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(max_length=120)),
                ('body', models.TextField()),
                ('isLiked', models.BooleanField(default=False)),
            ],
        ),
    ]
