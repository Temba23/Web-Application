# Generated by Django 5.0 on 2024-01-09 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='attachment1',
            field=models.FileField(blank=True, null=True, upload_to='audit/'),
        ),
        migrations.AddField(
            model_name='post',
            name='attachment2',
            field=models.FileField(blank=True, null=True, upload_to='audit/'),
        ),
    ]