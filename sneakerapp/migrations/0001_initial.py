# Generated by Django 4.2.2 on 2023-06-08 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Product Name')),
                ('cat', models.IntegerField(choices=[(1, 'Mobile'), (2, 'Clothes'), (3, 'Shoes')], verbose_name='Category')),
                ('price', models.FloatField(verbose_name='Product Price')),
                ('status', models.BooleanField(default=True)),
                ('pimage', models.ImageField(upload_to='image')),
            ],
        ),
    ]
