# Generated by Django 4.1.7 on 2023-04-11 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_rename_firstname_profile_firstname_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='lastname',
        ),
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(default='ad', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(default='ad', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='dob',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pix',
            field=models.ImageField(default='profile.jpg', upload_to='Profile'),
        ),
    ]
