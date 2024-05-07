# Generated by Django 3.2.12 on 2024-05-04 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advantage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100, verbose_name='Heading')),
                ('content', models.CharField(max_length=100, verbose_name='Content')),
                ('description', models.CharField(max_length=240, verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=50, verbose_name='Text')),
                ('url', models.SlugField(verbose_name='Url')),
            ],
        ),
    ]
