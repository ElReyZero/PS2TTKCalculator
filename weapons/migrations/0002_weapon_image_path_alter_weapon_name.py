# Generated by Django 4.0.5 on 2022-06-11 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weapons', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='weapon',
            name='image_path',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
