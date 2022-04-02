# Generated by Django 4.0.3 on 2022-03-05 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=120)),
                ('last_name', models.CharField(max_length=120)),
                ('document_id', models.CharField(max_length=30)),
                ('birth_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=50)),
                ('work_title', models.CharField(max_length=200)),
                ('company', models.CharField(max_length=200)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic_history.person')),
            ],
        ),
    ]