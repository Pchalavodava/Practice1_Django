from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import serializers
from .models import University, Course, UniversityCourse


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        read_only_fields = ['id']
        fields = ['name', 'country']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        read_only_fields = ['id']
        fields = ['title', 'description']


class UniversityCourseSerializer(serializers.ModelSerializer):
    university = UniversitySerializer()
    course = CourseSerializer()

    class Meta:
        model = UniversityCourse
        read_only_fields = ['id']
        fields = ['id', 'university', 'course', 'semester', 'duration_weeks']
        depth = 1


class UniversityCourseInfoSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='course.title')

    class Meta:
        model = UniversityCourse
        fields = ['title', 'semester', 'duration_weeks']


class UniversityWithCourseSerializer(serializers.ModelSerializer):
    courses = UniversityCourseInfoSerializer(source='universitycourse_set', many=True, read_only=True)

    class Meta:
        model = University
        fields = ['name', 'country', 'courses']