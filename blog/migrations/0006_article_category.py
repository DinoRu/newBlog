# Generated by Django 4.0.2 on 2022-02-07 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.CharField(default='Python', max_length=255),
        ),
    ]
