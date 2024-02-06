import uuid
from django.core.exceptions import ValidationError
from django.db import models

class Teacher(models.Model):
    employee_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    date_of_birth = models.CharField(max_length=10)
    age = models.IntegerField()
    Numberofclasses = models.IntegerField(default=0) 
    designation = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    experience = models.IntegerField()
    work = models.CharField(max_length=100, choices=[
        ('Class Handling', 'Class Handling'),
        ('Lab Supervision', 'Lab Supervision'),
        ('Extracurricular Activities', 'Extracurricular Activities')
    ])
    classtaking = models.CharField(max_length=100, choices=[
        ('Mathematics', 'Mathematics'),
        ('Science', 'Science'),
        ('English', 'English'),
        ('History', 'History'),
        ('Geography', 'Geography'),
        ('Physics', 'Physics'),
        ('Chemistry', 'Chemistry')
    ])
    major = models.CharField(max_length=100, choices=[
        ('Physics', 'Physics'),
        ('Chemistry', 'Chemistry'),
        ('Biology', 'Biology'),
        ('Mathematics', 'Mathematics'),
        ('English', 'English'),
        ('History', 'History'),
        ('Geography', 'Geography')
    ])

    def clean(self):
        if self.age <= 0:
            raise ValidationError({'age': 'Age must be a positive integer.'})
        if self.experience <= 0:
            raise ValidationError({'experience': 'Experience must be a positive integer.'})
