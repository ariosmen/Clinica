# Generated by Django 4.2.4 on 2023-09-05 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=50, verbose_name='Apellido')),
                ('dni', models.IntegerField(unique=True, verbose_name='DNI')),
                ('sexo', models.CharField(choices=[('', 'Seleccione una opcion'), ('Masculino', 'Masculino'), ('Femenino', 'Femenino')], max_length=10, verbose_name='Sexo')),
                ('direccion', models.CharField(max_length=50, verbose_name='Direccion')),
                ('telefono', models.CharField(max_length=50, verbose_name='Telefono')),
                ('email', models.EmailField(max_length=50, unique=True, verbose_name='Email')),
                ('estado_civil', models.CharField(choices=[('', 'Seleccione una opcion'), ('Soltero/a', 'Soltero/a'), ('Casado/a', 'Casado/a'), ('Viudo/a', 'Viudo/a'), ('Separado/a', 'Separado/a')], max_length=50, verbose_name='Estado Civil')),
                ('fecha_nacimiento', models.DateField(verbose_name='Fecha de Nac.')),
                ('obra_social', models.CharField(blank=True, max_length=50, null=True)),
                ('activo', models.BooleanField(default=True, verbose_name='Estado')),
                ('create', models.DateField(auto_now_add=True, verbose_name='Fecha de registro')),
            ],
            options={
                'verbose_name': 'paciente',
                'verbose_name_plural': 'pacientes',
                'db_table': 'pacientes',
                'ordering': ['apellido', 'nombre'],
            },
        ),
    ]
