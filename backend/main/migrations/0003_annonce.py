# Generated by Django 4.1 on 2022-09-02 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_city_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Annonce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('img', models.ImageField(null=True, upload_to='media/annonces')),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]