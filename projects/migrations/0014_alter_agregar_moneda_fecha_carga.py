# Generated by Django 4.1.1 on 2022-10-01 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0013_alter_agregar_moneda_fecha_carga'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agregar_moneda',
            name='fecha_carga',
            field=models.DateTimeField(),
        ),
    ]
