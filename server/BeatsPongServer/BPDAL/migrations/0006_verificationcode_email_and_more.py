# Generated by Django 4.2.11 on 2024-12-23 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BPDAL', '0005_verificationcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='verificationcode',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='verificationcode',
            name='expriarationDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
