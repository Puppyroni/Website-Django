# Generated by Django 5.0.2 on 2024-03-13 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0002_image_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='category',
            field=models.CharField(choices=[('TANK', 'Tank'), ('MELEE DPS', 'Melee DPS'), ('RANGED DPS', 'Ranged DPS'), ('MAGICAL DPS', 'Magical DPS'), ('HEALER', 'Healer')], default='', max_length=100),
        ),
    ]
