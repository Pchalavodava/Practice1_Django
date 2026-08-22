from django.contrib import admin

from . import models


@admin.register(models.University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(models.UniversityCourse)
class UniversityCourseAdmin(admin.ModelAdmin):
    list_display = ['university', 'course', 'semester', 'duration_weeks']

