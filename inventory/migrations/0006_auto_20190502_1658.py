# Generated by Django 2.2 on 2019-05-02 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_auto_20190502_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='content_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
        ),
        migrations.AlterField(
            model_name='device',
            name='object_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]