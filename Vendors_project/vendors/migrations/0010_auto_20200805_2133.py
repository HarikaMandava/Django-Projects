# Generated by Django 3.0.7 on 2020-08-05 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0009_contacts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacts',
            name='vendor',
        ),
        migrations.AddField(
            model_name='contacts',
            name='vendor',
            field=models.ManyToManyField(to='vendors.Vendors'),
        ),
    ]
