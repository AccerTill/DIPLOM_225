# Generated by Django 4.1.7 on 2023-03-28 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sorting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('genre_author', models.CharField(max_length=500)),
                ('picture', models.ImageField(upload_to='sorting/images/')),
                ('links', models.URLField(blank=True)),
            ],
        ),
    ]
