# Generated by Django 2.1.2 on 2018-12-06 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classdoor', '0015_auto_20181204_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='averageGrade',
            field=models.CharField(blank=True, choices=[('a', 'A'), ('a-', 'A-'), ('b+', 'B+'), ('b', 'B'), ('b-', 'B-'), ('c+', 'C+'), ('c', 'C'), ('c-', 'C-'), ('d+', 'D+'), ('d', 'D'), ('d', 'D-'), ('f', 'F')], max_length=2),
        ),
        migrations.AlterField(
            model_name='course',
            name='starRating',
            field=models.CharField(choices=[('5', '5'), ('4', '4'), ('3', '3'), ('2', '2'), ('1', '1')], max_length=3),
        ),
    ]
