from django.db import models
from django.core.validators import MinValueValidator


class University(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} - {self.country}'


class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)

    def __str__(self):
        return f'{self.title}'


class UniversityCourse(models.Model):
    SEMESTERS = [
        ('S26', 'Spring 2026'),
        ('W26', 'Winter 2026'),
        ('S27', 'Spring 2027')
    ]
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.CharField(max_length=50, choices=SEMESTERS, default='S26')
    duration_weeks = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['university', 'course', 'semester'],
                                    name='unique_university_course_semester')
        ]

    def __str__(self):
        return f'{self.university}: {self.course} - {self.semester}. Duration: {self.duration_weeks}'


