# Generated by Django 5.1.3 on 2024-11-09 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutritions', '0012_remove_userinfo_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='name',
            field=models.CharField(default='NoName', max_length=100),
        ),
    ]
