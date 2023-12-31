# Generated by Django 3.0.2 on 2020-03-06 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0008_auto_20200306_1527'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='programsapplied',
            name='candidate_id',
        ),
        migrations.RemoveField(
            model_name='programsapplied',
            name='program_id',
        ),
        migrations.AddField(
            model_name='programsapplied',
            name='candidate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='frontend.Candidates'),
        ),
        migrations.AddField(
            model_name='programsapplied',
            name='program',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='frontend.Programs'),
        ),
        migrations.AlterField(
            model_name='programs',
            name='committee_member',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='frontend.CommitteeMembers'),
        ),
        migrations.AlterField(
            model_name='programs',
            name='judge',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='frontend.Judges'),
        ),
    ]
