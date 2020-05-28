# Generated by Django 3.0.6 on 2020-05-19 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('run', '0004_auto_20200519_1637'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='event_name',
        ),
        migrations.RemoveField(
            model_name='event',
            name='event_number',
        ),
        migrations.RemoveField(
            model_name='event',
            name='heat_number',
        ),
        migrations.RemoveField(
            model_name='event',
            name='round_number',
        ),
        migrations.RemoveField(
            model_name='eventdata',
            name='event',
        ),
        migrations.AddField(
            model_name='event',
            name='name',
            field=models.CharField(default='Event', max_length=64, verbose_name='Название события'),
        ),
        migrations.CreateModel(
            name='EventDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_number', models.IntegerField(verbose_name='Номер события')),
                ('round_number', models.IntegerField(verbose_name='Номер круга')),
                ('heat_number', models.IntegerField(verbose_name='Номер забега')),
                ('event', models.ForeignKey(default='Event', on_delete=django.db.models.deletion.CASCADE, to='run.Event', verbose_name='Событие')),
            ],
        ),
        migrations.AddField(
            model_name='eventdata',
            name='event_detail',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='run.EventDetail', verbose_name='Событие'),
        ),
    ]
