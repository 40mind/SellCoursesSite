# Generated by Django 3.2.7 on 2021-10-24 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='direction',
            old_name='name',
            new_name='Название',
        ),
    ]
