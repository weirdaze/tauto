# Generated by Django 2.2 on 2019-06-04 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('device_model', '0009_auto_20190604_1931'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chipmodel',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='chipmodel',
            name='object_id',
        ),
        migrations.AddField(
            model_name='chipmodel',
            name='module_build',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='device_model.ModuleBuild'),
        ),
        migrations.AlterField(
            model_name='chipmodel',
            name='chip',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='device_model.Chip'),
        ),
    ]