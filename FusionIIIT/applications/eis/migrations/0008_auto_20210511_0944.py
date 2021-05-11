# Generated by Django 3.1.5 on 2021-05-11 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eis', '0007_auto_20210422_0141'),
    ]

    operations = [
        migrations.AddField(
            model_name='emp_achievement',
            name='achievment_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='emp_consultancy_projects',
            name='remarks',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='emp_consultancy_projects',
            name='status',
            field=models.CharField(blank=True, choices=[('Completed', 'Completed'), ('Submitted', 'Submitted'), ('Ongoing', 'Ongoing')], default='Ongoing', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='emp_mtechphd_thesis',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='emp_mtechphd_thesis',
            name='semester',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AddField(
            model_name='emp_mtechphd_thesis',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='emp_mtechphd_thesis',
            name='status',
            field=models.CharField(blank=True, choices=[('Awarded', 'Awarded'), ('Submitted', 'Submitted'), ('Ongoing', 'Ongoing'), ('Completed', 'Completed')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='emp_patents',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='emp_patents',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='emp_published_books',
            name='publication_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='emp_session_chair',
            name='remarks',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AddField(
            model_name='emp_techtransfer',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='emp_techtransfer',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='emp_achievement',
            name='pf_no',
            field=models.IntegerField(),
        ),
    ]
