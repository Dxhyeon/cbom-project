# Generated by Django 4.2.5 on 2023-10-25 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sbom_app', '0006_searche_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearcheData',
            fields=[
                ('id', models.BigIntegerField(primary_key='True', serialize=False)),
                ('cve_id', models.CharField(blank=True, db_column='CVE_ID', max_length=20, null=True)),
                ('product', models.CharField(blank=True, max_length=100, null=True)),
                ('version', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'searche_data',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='searche_data',
        ),
    ]
