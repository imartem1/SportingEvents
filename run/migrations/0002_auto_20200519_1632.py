# Generated by Django 3.0.6 on 2020-05-19 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('run', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventdata',
            name='time',
            field=models.CharField(max_length=8, verbose_name='Время'),
        ),
    ]
