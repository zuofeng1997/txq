# Generated by Django 2.0.5 on 2018-06-25 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_auto_20180625_0744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follow',
            name='user2',
            field=models.ManyToManyField(blank=True, related_name='user2', to='login.User'),
        ),
    ]
