# Generated by Django 2.2 on 2019-05-14 17:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.png', upload_to='profile_pics')),
                ('phone', models.CharField(blank=True, max_length=50)),
                ('company', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('code', models.CharField(blank=True, default='xx', max_length=200)),
                ('active', models.BooleanField(default=False)),
                ('accepted_eula', models.BooleanField(default=True)),
                ('user', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
