# Generated by Django 3.1.1 on 2021-02-27 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='/tmp.jpg', null=True, upload_to=''),
        ),
    ]
