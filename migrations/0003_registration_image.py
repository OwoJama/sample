# Generated by Django 4.2.5 on 2023-10-17 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0002_registration_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='image',
            field=models.ImageField(default='image', upload_to='', verbose_name='./images/Fuhad_image.jpeg'),
        ),
    ]
