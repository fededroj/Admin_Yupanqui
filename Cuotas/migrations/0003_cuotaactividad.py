# Generated by Django 4.2.4 on 2023-11-01 00:47

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Administracion', '0002_remove_categoria_socio'),
        ('Socios', '0001_initial'),
        ('Cuotas', '0002_alter_cuotamensual_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CuotaActividad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mes', models.IntegerField(choices=[(1, 'Enero'), (2, 'Febrero'), (3, 'Marzo'), (4, 'Abril'), (5, 'Mayo'), (6, 'Junio'), (7, 'Julio'), (8, 'Agosto'), (9, 'Sepiembre'), (10, 'Octubre'), (11, 'Noviembre'), (12, 'Diciembre')])),
                ('ano', models.IntegerField(default=2023)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_pago', models.DateField(default=datetime.date.today)),
                ('actividad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Administracion.actividad')),
                ('socio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Socios.socio')),
            ],
        ),
    ]
