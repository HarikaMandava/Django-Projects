# Generated by Django 3.0.7 on 2020-08-05 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0008_auto_20200805_1510'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, null=True)),
                ('last_name', models.CharField(blank=True, max_length=17)),
                ('title', models.CharField(blank=True, max_length=17)),
                ('desk_phone', models.CharField(max_length=20, null=True)),
                ('email', models.CharField(max_length=20, null=True)),
                ('speciality', models.CharField(max_length=200, null=True)),
                ('vendor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vendors.Vendors')),
            ],
        ),
    ]