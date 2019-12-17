# Generated by Django 3.0 on 2019-12-15 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopping',
            name='title',
        ),
        migrations.AddField(
            model_name='shopping',
            name='body',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shopping',
            name='mail',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]
