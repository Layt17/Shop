# Generated by Django 3.2.7 on 2021-09-11 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_remove_smartphone_sd'),
    ]

    operations = [
        migrations.AddField(
            model_name='smartphone',
            name='sd',
            field=models.BooleanField(default=True, verbose_name='Наличие слота sd'),
        ),
    ]
