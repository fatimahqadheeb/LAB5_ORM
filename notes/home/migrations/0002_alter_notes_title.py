# Generated by Django 4.1.1 on 2022-09-14 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='title',
            field=models.CharField(max_length=2048),
        ),
    ]
