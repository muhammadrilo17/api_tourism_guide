# Generated by Django 3.0.6 on 2020-07-17 07:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pariwisataapi', '0004_remove_pariwisata_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='pariwisata',
            name='images',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='', verbose_name='images/'),
            preserve_default=False,
        ),
    ]