# Generated by Django 5.0.2 on 2024-03-04 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('caption', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('img', models.CharField(max_length=100)),
            ],
        ),
    ]
