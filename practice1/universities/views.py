from django.db.models import Avg
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import response
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import University, Course, UniversityCourse
from .serializers import UniversitySerializer, CourseSerializer, UniversityCourseSerializer, UniversityWithCourseSerializer


class UniversityViewSet(ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer

    @action(detail=True, methods=['get'], url_path='course-stats', url_name='course-stats')
    def course_stats(self, request, pk=None):
        university = self.get_object()
        total_courses = UniversityCourse.objects.filter(university=university).values('course').distinct().count()
        average_duration = UniversityCourse.objects.filter(university=university).aggregate(Avg('duration_weeks'))
        return Response({
            'total_courses': total_courses,
            'average_duration': average_duration['duration_weeks__avg']
        })

class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class UniversityCourseViewSet(ModelViewSet):
    queryset = UniversityCourse.objects.order_by('duration_weeks')
    serializer_class = UniversityCourseSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter]

    search_fields = ['university__name', 'course__title']
    ordering_fields = ['duration_weeks']
    filterset_fields = {
        'semester': ['exact', 'in'],
        'course__title': ['exact', 'icontains'],
    }


class UniversityCoursesView(RetrieveAPIView):
    serializer_class = UniversityWithCourseSerializer
    filter_backends = [SearchFilter]

    def get_queryset(self):
        return University.objects.prefetch_related('universitycourse_set__course')

    lookup_field = 'id'
    lookup_url_kwarg = 'university_id'
