from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views


router = DefaultRouter()
router.register('universities', views.UniversityViewSet, basename='university')
router.register('courses', views.CourseViewSet)
router.register('universities-courses', views.UniversityCourseViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('universities/<int:university_id>/courses/', views.UniversityCoursesView.as_view(), name='university-courses')
]

