# Generated by Django 3.0.5 on 2020-04-15 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0004_auto_20200415_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='regularuser',
            name='balance',
            field=models.BigIntegerField(null=True),
        ),
    ]