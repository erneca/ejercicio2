# Generated by Django 4.1.1 on 2022-10-01 13:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0007_alter_agregar_moneda_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agregar_moneda',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
