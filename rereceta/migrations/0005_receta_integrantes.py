# Generated by Django 2.2.6 on 2019-11-01 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rereceta', '0004_integrante'),
    ]

    operations = [
        migrations.AddField(
            model_name='receta',
            name='integrantes',
            field=models.ManyToManyField(to='rereceta.Integrante'),
        ),
    ]