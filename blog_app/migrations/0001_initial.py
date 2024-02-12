# Generated by Django 3.1 on 2024-02-12 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=255, verbose_name='Put a Title')),
                ('blog_content', models.TextField(verbose_name='Blog Content Write Here')),
                ('blog_image', models.ImageField(blank=True, null=True, upload_to='blog_images', verbose_name='Image')),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-publish_date'],
            },
        ),
    ]
