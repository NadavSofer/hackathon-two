# Generated by Django 4.2 on 2023-06-01 09:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0004_userprofile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='palettes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_1', models.CharField(max_length=50)),
                ('color_2', models.CharField(max_length=50)),
                ('color_3', models.CharField(max_length=50)),
                ('color_4', models.CharField(max_length=50)),
                ('color_5', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
