# Generated by Django 3.2.3 on 2021-06-03 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_auto_20210603_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='internship_completion_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=10),
        ),
        migrations.AlterField(
            model_name='student',
            name='status_of_project',
            field=models.CharField(choices=[('Incomplete', 'Incomplete'), ('Partially Completed', 'Partially Completed'), ('Completed', 'Completed')], default='Incomplete', max_length=100),
        ),
    ]