# Generated by Django 2.2 on 2019-05-10 15:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 10, 15, 5, 1, 719102, tzinfo=utc), verbose_name='Fecha de publicación'),
        ),
    ]
