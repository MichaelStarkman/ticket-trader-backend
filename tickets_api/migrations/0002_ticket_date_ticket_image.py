# Generated by Django 4.0.4 on 2022-04-12 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='date',
            field=models.DateTimeField(default='2022-01-01'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='image',
            field=models.CharField(default='https://i.imgur.com/A79Xirs.jpeg', max_length=100),
        ),
    ]
