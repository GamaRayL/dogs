# Generated by Django 4.2.5 on 2023-09-18 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_alter_breed_options_alter_dog_breed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='birth_date',
            field=models.DateField(blank=True, null=True, verbose_name='дата рождения'),
        ),
    ]
