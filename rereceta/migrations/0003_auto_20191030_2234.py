# Generated by Django 2.2.6 on 2019-10-31 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rereceta', '0002_auto_20191030_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='imagen',
            field=models.ImageField(default=None, upload_to='ropa'),
        ),
    ]