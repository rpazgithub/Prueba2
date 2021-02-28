# Generated by Django 3.1.6 on 2021-02-23 16:37

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActividadEconomica',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=80, verbose_name='Actividad economica*:')),
            ],
            options={
                'verbose_name_plural': 'Actividades economicas',
            },
        ),
        migrations.CreateModel(
            name='EtapaProyecto',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30, null=True, verbose_name='Etapa actual del proyecto*:')),
            ],
            options={
                'verbose_name_plural': 'Etapas de proyectos',
            },
        ),
        migrations.CreateModel(
            name='ProyectoEmpresarial',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=60, verbose_name='Nombre del proyecto*:')),
                ('descripcion', models.TextField(verbose_name='Descripcion del proyecto*:')),
                ('fecha_inicio', models.DateField(blank=True, help_text='Escriba o seleccione la fecha de inicio del proyecto', null=True, verbose_name='Inicio del proyecto:')),
                ('cantidad_empleados', models.IntegerField(blank=True, null=True, verbose_name='Numero de empleados:')),
                ('facturacion_mensual_aprox', models.IntegerField(blank=True, help_text='Valor aproximado de facturacion mensual', null=True, verbose_name='Facturacion mensual:')),
                ('productos', models.TextField(blank=True, null=True)),
                ('servicios', models.TextField(blank=True, null=True)),
                ('tipo_mercado', models.CharField(blank=True, max_length=5, null=True, verbose_name='Tipo de mercado:')),
                ('numero_integrantes', models.CharField(blank=True, max_length=3, null=True, verbose_name='Cantidad de integrantes:')),
                ('actividad_economica', models.ForeignKey(blank=True, help_text='Seleccione una actividad economica', null=True, on_delete=django.db.models.deletion.SET_NULL, to='aplicacion.actividadeconomica')),
                ('etapa_id', models.ForeignKey(blank=True, help_text='Identifique la etapa en la cual se encuentra el proyecto', null=True, on_delete=django.db.models.deletion.SET_NULL, to='aplicacion.etapaproyecto')),
                ('persona_contacto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aplicacion.proyectoempresarial', verbose_name='Persona contacto:')),
            ],
            options={
                'verbose_name_plural': 'Proyectos empresariales',
            },
        ),
    ]
