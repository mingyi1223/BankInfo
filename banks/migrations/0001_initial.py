# Generated by Django 5.0.6 on 2024-06-24 12:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_code', models.CharField(max_length=50)),
                ('bank', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Branches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_code', models.CharField(max_length=50, null=True)),
                ('branch', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('tel', models.CharField(max_length=20)),
                ('head_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banks.banks')),
            ],
        ),
    ]
