# Generated by Django 3.2.5 on 2023-11-06 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalyst', '0002_alter_file_existingpath'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='existingPath',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
