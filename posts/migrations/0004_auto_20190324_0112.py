# Generated by Django 2.1.1 on 2019-03-23 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_postadd_random_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postadd',
            name='pub_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='postadd',
            name='random_link',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]
