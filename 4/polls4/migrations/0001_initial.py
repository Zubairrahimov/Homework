# Generated by Django 4.2.5 on 2023-09-15 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=100)),
                ('second_name', models.CharField(max_length=100)),
                ('job', models.CharField(max_length=100)),
            ],
        ),
    ]
