# Generated by Django 4.2.4 on 2023-08-17 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cvs_app', '0012_academic_data_created_at_academic_data_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='empresa',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='puesto',
            field=models.CharField(blank=True, max_length=180, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='referencia_nombre',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='referencia_puesto',
            field=models.CharField(blank=True, max_length=180, null=True),
        ),
    ]