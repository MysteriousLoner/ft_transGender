# Generated by Django 4.2.11 on 2024-12-11 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BPDAL', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('profilePicture', models.ImageField(upload_to='profile_pics/')),
            ],
        ),
    ]
