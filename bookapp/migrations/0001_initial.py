# Generated by Django 4.1.4 on 2023-07-05 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
                ('author', models.CharField(max_length=100)),
                ('Created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]