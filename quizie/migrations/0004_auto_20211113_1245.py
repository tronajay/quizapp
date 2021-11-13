# Generated by Django 2.2.24 on 2021-11-13 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizie', '0003_questions_quiz'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('correct', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('desc', models.TextField()),
                ('quiz', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='quizie.Quiz')),
            ],
        ),
        migrations.RemoveField(
            model_name='questions',
            name='options',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='quiz',
        ),
        migrations.DeleteModel(
            name='Answers',
        ),
        migrations.DeleteModel(
            name='Questions',
        ),
        migrations.AddField(
            model_name='answer',
            name='questions',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizie.Question'),
        ),
    ]
