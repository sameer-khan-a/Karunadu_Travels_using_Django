# Generated by Django 4.1.1 on 2022-09-17 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('Address', models.TextField(max_length=122)),
                ('Zip', models.CharField(max_length=6)),
                ('Package', models.CharField(max_length=30)),
            ],
        ),
    ]
