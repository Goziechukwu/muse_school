# Generated by Django 3.2.25 on 2024-06-04 22:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_userprofile_id'),
        ('checkout', '0002_alter_order_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user_profile',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='orders',
                to='profiles.userprofile'
            ),
        ),
    ]
