# Generated by Django 2.1.1 on 2019-03-25 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_user_save'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_save',
            name='delete_post',
        ),
        migrations.DeleteModel(
            name='User_Save',
        ),
    ]
