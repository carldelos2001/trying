# Generated by Django 4.2 on 2024-01-12 08:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('my_final', '0009_userextend2_remove_patients_patient_blood_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userextend2',
            name='patient',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
