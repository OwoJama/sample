# Generated by Django 4.2.5 on 2023-10-15 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='message',
            field=models.TextField(default='Welcome', max_length=500),
        ),
    ]
