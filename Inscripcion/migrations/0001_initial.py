# Generated by Django 4.2 on 2023-11-11 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Administracion', '0004_profesor_actividad'),
        ('Socios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inscripcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inscripcion', models.DateField(auto_now_add=True, verbose_name='Fecha de Inscripcion')),
                ('actividad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Administracion.actividad', verbose_name='Actividad')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Administracion.categoria', verbose_name='Categoria')),
                ('socio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Socios.socio', verbose_name='Socio')),
            ],
        ),
    ]
