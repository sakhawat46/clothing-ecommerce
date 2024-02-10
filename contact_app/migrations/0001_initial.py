# Generated by Django 3.1 on 2022-05-12 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=250)),
                ('mobile', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]