# Generated by Django 3.1.6 on 2021-02-23 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0003_auto_20210223_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyectoempresarial',
            name='persona_contacto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='proyectoempresarial', to='aplicacion.proyectoempresarial', verbose_name='Persona contacto:'),
        ),
    ]
