# Generated by Django 5.1.4 on 2024-12-07 19:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stand_users', '0002_rename_stand_user_standuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stand',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='stand_users.standuser'),
        ),
    ]
