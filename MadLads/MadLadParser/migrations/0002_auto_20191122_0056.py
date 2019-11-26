# Generated by Django 2.2.7 on 2019-11-22 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MadLadParser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='story_array',
            field=models.CharField(default=None, max_length=1500),
        ),
        migrations.AlterField(
            model_name='story',
            name='story_name',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='story',
            name='story_text',
            field=models.CharField(default=None, max_length=1500),
        ),
    ]
