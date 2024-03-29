# Generated by Django 5.0 on 2024-01-09 06:14

import django.core.validators
import re
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name_plural': 'Profile'},
        ),
        migrations.AddField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone_no',
            field=models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\d+)*\\Z'), code='invalid', message=None), django.core.validators.MinLengthValidator(10)], verbose_name='Phone number'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pp',
            field=models.ImageField(default='lbj.jpg', upload_to='profile_pics'),
        ),
    ]
