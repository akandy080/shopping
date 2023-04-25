# Generated by Django 4.1.7 on 2023-04-04 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_delete_prduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('img', models.ImageField(default='product.jpg', upload_to='Product')),
                ('price', models.FloatField()),
                ('brand', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('date_uploaded', models.DateField(auto_now=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.category')),
            ],
        ),
    ]
