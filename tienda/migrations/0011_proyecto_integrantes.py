# Generated by Django 2.2.3 on 2019-10-09 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0010_integrante'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='integrantes',
            field=models.ManyToManyField(to='tienda.Integrante'),
        ),
    ]