# Generated by Django 3.0.2 on 2020-03-06 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0006_programs_judge'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgramsApplied',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('program_id', models.IntegerField(null=True)),
                ('candidate_id', models.IntegerField(null=True)),
            ],
        ),
    ]
