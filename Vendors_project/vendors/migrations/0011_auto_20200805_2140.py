# Generated by Django 3.0.7 on 2020-08-05 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0010_auto_20200805_2133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacts',
            name='vendor',
        ),
        migrations.AddField(
            model_name='contacts',
            name='vendor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vendors.Vendors'),
        ),
    ]