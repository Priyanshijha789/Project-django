# Generated by Django 5.2 on 2025-05-01 12:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0005_alter_doctor_is_approved'),
        ('staff', '0002_bill_labreport'),
    ]

    operations = [
        migrations.CreateModel(
            name='DischargeRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=20)),
                ('admission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.patientadmission')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctors.doctor')),
            ],
        ),
    ]
