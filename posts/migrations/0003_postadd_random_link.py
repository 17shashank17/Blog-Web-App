# Generated by Django 2.1.1 on 2019-03-23 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_postadd_heading'),
    ]

    operations = [
        migrations.AddField(
            model_name='postadd',
            name='random_link',
            field=models.CharField(default='', max_length=200),
        ),
    ]
