# Generated by Django 3.1.6 on 2021-03-21 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='notes.category'),
        ),
    ]