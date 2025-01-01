# Generated by Django 5.0.2 on 2024-03-06 13:28

import datetime
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogindexpage',
            name='body',
            field=wagtail.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='blogindexpage',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name='Post date'),
        ),
        migrations.AlterField(
            model_name='blogindexpage',
            name='intro',
            field=models.CharField(max_length=250),
        ),
    ]
