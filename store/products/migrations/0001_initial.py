# Generated by Django 4.1.4 on 2023-02-11 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('descrition', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='category_images')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('amount', models.PositiveIntegerField(default=0)),
                ('image', models.ImageField(upload_to='images')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.category')),
            ],
        ),
    ]