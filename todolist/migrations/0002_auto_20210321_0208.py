# Generated by Django 3.1.4 on 2021-03-20 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_info',
            name='age',
            field=models.IntegerField(),
        ),
    ]
