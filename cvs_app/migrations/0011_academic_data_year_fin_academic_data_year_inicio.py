# Generated by Django 4.2.4 on 2023-08-17 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cvs_app', '0010_alter_profile_cantidad_hijos_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='academic_data',
            name='year_fin',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='academic_data',
            name='year_inicio',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
    ]
