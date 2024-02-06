# Generated by Django 4.2.9 on 2024-02-05 16:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('employee_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('date_of_birth', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('Numberofclasses', models.IntegerField(default=0)),
                ('designation', models.CharField(max_length=100)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('experience', models.IntegerField()),
                ('work', models.CharField(choices=[('Class Handling', 'Class Handling'), ('Lab Supervision', 'Lab Supervision'), ('Extracurricular Activities', 'Extracurricular Activities')], max_length=100)),
                ('classtaking', models.CharField(choices=[('Mathematics', 'Mathematics'), ('Science', 'Science'), ('English', 'English'), ('History', 'History'), ('Geography', 'Geography'), ('Physics', 'Physics'), ('Chemistry', 'Chemistry')], max_length=100)),
                ('major', models.CharField(choices=[('Physics', 'Physics'), ('Chemistry', 'Chemistry'), ('Biology', 'Biology'), ('Mathematics', 'Mathematics'), ('English', 'English'), ('History', 'History'), ('Geography', 'Geography')], max_length=100)),
            ],
        ),
    ]