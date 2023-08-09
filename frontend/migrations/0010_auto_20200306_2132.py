# Generated by Django 3.0.2 on 2020-03-06 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0009_auto_20200306_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='programsapplied',
            name='attended',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=7),
        ),
        migrations.AddField(
            model_name='programsapplied',
            name='marks',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
    ]
