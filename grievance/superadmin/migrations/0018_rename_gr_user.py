# Generated by Django 4.1.7 on 2023-04-09 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0017_gr_delete_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='gr',
            new_name='user',
        ),
    ]