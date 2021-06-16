# Generated by Django 3.2.4 on 2021-06-16 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wiki',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('link', models.URLField()),
                ('no_of_image', models.PositiveSmallIntegerField()),
                ('no_of_link', models.PositiveSmallIntegerField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]