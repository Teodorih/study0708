# Generated by Django 3.2.5 on 2021-07-15 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]