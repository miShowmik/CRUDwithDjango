# Generated by Django 3.1.3 on 2020-11-27 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='course_code',
            field=models.IntegerField(default=213),
            preserve_default=False,
        ),
    ]