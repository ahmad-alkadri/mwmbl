# Generated by Django 4.2.11 on 2024-03-09 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mwmbl', '0005_oldindex'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oldindex',
            name='index_total_pages',
        ),
        migrations.AlterField(
            model_name='oldindex',
            name='last_copied_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='oldindex',
            name='last_page_copied',
            field=models.IntegerField(null=True),
        ),
    ]