# Generated by Django 2.2 on 2019-06-04 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('device_model', '0007_auto_20190604_1907'),
    ]

    operations = [
        migrations.AddField(
            model_name='chip',
            name='fif_serdes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='fif_serdes', to='device_model.Serdes'),
        ),
        migrations.AddField(
            model_name='chip',
            name='fif_serdes_num',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='chip',
            name='nif_serdes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='nif_serdes', to='device_model.Serdes'),
        ),
        migrations.AddField(
            model_name='chip',
            name='nif_serdes_num',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
