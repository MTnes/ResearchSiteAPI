# Generated by Django 2.2.13 on 2021-04-17 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254)),
                ('description', models.TextField(blank=True)),
                ('imagePath', models.ImageField(blank=True, null=True, upload_to='people_pic')),
            ],
        ),
    ]