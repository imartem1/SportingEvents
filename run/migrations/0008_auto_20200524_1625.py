# Generated by Django 3.0.6 on 2020-05-24 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('run', '0007_auto_20200524_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventdata',
            name='edu_number',
            field=models.CharField(max_length=8, null=True, verbose_name='Номер образовательного учереждения'),
        ),
        migrations.AlterField(
            model_name='eventdata',
            name='person_id',
            field=models.CharField(max_length=8, null=True, verbose_name='Номер участника'),
        ),
    ]
