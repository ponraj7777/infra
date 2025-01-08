# Generated by Django 5.1.4 on 2025-01-05 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auditortaskdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tech_ID', models.CharField(default='', max_length=20)),
                ('name', models.CharField(default='', max_length=100)),
                ('area', models.CharField(default='', max_length=20)),
                ('Deadline', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=20)),
                ('Age', models.IntegerField(default='')),
                ('Address', models.CharField(default='', max_length=20)),
                ('Contact', models.IntegerField(default='')),
                ('Email', models.CharField(default='', max_length=20)),
            ],
        ),
    ]