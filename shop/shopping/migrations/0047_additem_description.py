# Generated by Django 3.0 on 2020-01-02 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0046_auto_20200102_2226'),
    ]

    operations = [
        migrations.AddField(
            model_name='additem',
            name='description',
            field=models.TextField(default='lol'),
        ),
    ]
