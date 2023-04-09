# Generated by Django 4.1.7 on 2023-04-09 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0016_alter_registration_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='gr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.TextField(max_length=20)),
                ('surName', models.TextField(max_length=20)),
                ('fatherName', models.TextField(max_length=20)),
                ('semester', models.IntegerField()),
                ('phoneNumber', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=100)),
                ('Collage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='superadmin.collage')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='superadmin.department')),
                ('designation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='superadmin.designation')),
            ],
        ),
        migrations.DeleteModel(
            name='user',
        ),
    ]