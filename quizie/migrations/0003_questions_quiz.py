# Generated by Django 2.2.24 on 2021-11-13 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizie', '0002_answers_questions'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='quiz',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='quizie.Quiz'),
        ),
    ]
