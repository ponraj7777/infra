# Generated by Django 5.1.4 on 2025-01-05 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admintaskdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Audi_ID', models.CharField(default='', max_length=20)),
                ('name', models.CharField(default='', max_length=100)),
                ('area', models.CharField(default='', max_length=20)),
                ('Deadline', models.DateField()),
            ],
        ),
    ]