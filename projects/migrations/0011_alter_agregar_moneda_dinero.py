# Generated by Django 4.1.1 on 2022-10-01 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_alter_agregar_moneda_dinero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agregar_moneda',
            name='dinero',
            field=models.FloatField(max_length=200),
        ),
    ]