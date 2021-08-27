# Generated by Django 3.2.6 on 2021-08-27 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('USERMODEL', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]