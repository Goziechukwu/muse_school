# Generated by Django 3.2.25 on 2024-07-27 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_instructor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='instructors/'),
        ),
    ]
