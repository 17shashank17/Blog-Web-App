# Generated by Django 2.1.1 on 2019-03-23 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postadd',
            name='heading',
            field=models.CharField(default='', max_length=200),
        ),
    ]
