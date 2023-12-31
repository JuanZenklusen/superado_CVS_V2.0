# Generated by Django 4.2.4 on 2023-08-14 22:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cvs_app', '0009_academic_level_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cantidad_hijos',
            field=models.CharField(blank=True, default='0', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='estado_civil',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='genero',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='localidad',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='nacionalidad',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='provincia',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='telefono',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.CreateModel(
            name='Academic_Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('escuela', models.CharField(blank=True, max_length=80, null=True)),
                ('titulo', models.CharField(blank=True, max_length=150, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=250, null=True)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cvs_app.status')),
                ('nivel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cvs_app.academic_level')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
