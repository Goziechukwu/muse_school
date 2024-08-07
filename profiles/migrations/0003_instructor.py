# Generated by Django 3.2.25 on 2024-07-27 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_userprofile_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('bio', models.TextField()),
                ('photo', models.ImageField(upload_to='instructors/')),
                ('specialization', models.CharField(max_length=100)),
                ('availability', models.CharField(max_length=100)),
                ('contact_info', models.CharField(max_length=200)),
            ],
        ),
    ]
