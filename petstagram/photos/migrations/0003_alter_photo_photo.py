# Generated by Django 4.2.1 on 2023-05-29 18:54

from django.db import migrations, models
import petstagram.photos.validators


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_alter_photo_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(upload_to='images', validators=[petstagram.photos.validators.validate_file_size]),
        ),
    ]