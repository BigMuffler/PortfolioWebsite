# Generated by Django 3.2.3 on 2021-05-24 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20210524_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='paperLink',
            field=models.FilePathField(default='1', path='/other'),
            preserve_default=False,
        ),
    ]