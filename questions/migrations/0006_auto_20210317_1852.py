# Generated by Django 3.1.6 on 2021-03-17 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0005_questionview'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questionview',
            old_name='IPAddres',
            new_name='IPAddress',
        ),
    ]
