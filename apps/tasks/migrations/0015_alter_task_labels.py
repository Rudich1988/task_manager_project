# Generated by Django 5.0.4 on 2024-04-21 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0003_remove_label_tasks'),
        ('tasks', '0014_alter_task_labels'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='labels',
            field=models.ManyToManyField(blank=True, to='labels.label', verbose_name='Метки'),
        ),
    ]
