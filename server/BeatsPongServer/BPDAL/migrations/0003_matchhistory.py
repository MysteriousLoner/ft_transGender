# Generated by Django 4.2.11 on 2024-12-13 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BPDAL', '0002_profiledata'),
    ]

    operations = [
        migrations.CreateModel(
            name='MatchHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('winRate', models.FloatField()),
                ('bestFriend', models.CharField(max_length=100)),
            ],
        ),
    ]
