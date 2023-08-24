# Generated by Django 2.2.7 on 2021-05-08 15:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('file', models.FileField(default='file', upload_to='post_files')),
                ('filetype', models.CharField(max_length=150)),
                ('text', models.CharField(max_length=10000)),
                ('uploaded', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]