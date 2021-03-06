# Generated by Django 3.1.5 on 2021-01-19 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='pics')),
                ('category', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('content', models.TextField()),
            ],
        ),
    ]
