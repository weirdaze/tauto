# Generated by Django 2.2 on 2019-06-04 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('device_model', '0004_chipmodelno_code_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chip',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='chip',
            name='object_id',
        ),
        migrations.CreateModel(
            name='ChipModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('chip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='device_model.Chip')),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
        ),
    ]
