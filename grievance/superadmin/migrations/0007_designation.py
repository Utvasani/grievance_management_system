# Generated by Django 4.1.7 on 2023-03-27 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0006_rename_vinit_collage'),
    ]

    operations = [
        migrations.CreateModel(
            name='designation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designationName', models.TextField(max_length=30, unique=True)),
                ('power', models.IntegerField(unique=True)),
            ],
        ),
    ]
