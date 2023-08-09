# Generated by Django 3.0.2 on 2020-03-05 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_auto_20200213_0020'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidates',
            name='profile_image',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='candidates',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('suspend', 'Suspend')], default='active', max_length=7),
        ),
        migrations.AlterField(
            model_name='candidates',
            name='username',
            field=models.CharField(max_length=100, null=True),
        ),
    ]