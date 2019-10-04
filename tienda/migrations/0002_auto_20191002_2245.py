# Generated by Django 2.2.3 on 2019-10-03 04:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proyecto',
            name='proyecto',
        ),
        migrations.AddField(
            model_name='categoria',
            name='proyecto',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='tienda.Proyecto'),
        ),
    ]