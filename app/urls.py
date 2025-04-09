from django.urls import path

from .views import ( CourseAPIView, CourseRetrieveAPIView, CourseUpdateAPIView,
CourseDestroyAPIView, CourseCreateAPIView)

urlpatterns = [
    path('courses/', CourseAPIView.as_view()),
    # path('courses/<int:pk>/', CourseDetailAPIview.as_view()),
    path('courses/create/', CourseCreateAPIView.as_view()),
    path('courses/retrieve/', CourseRetrieveAPIView.as_view()),
    path('courses/update/', CourseUpdateAPIView.as_view()),
    path('courses/destroy/', CourseDestroyAPIView.as_view()),

    # path('lessons/', LessonApiView.as_view()),
]

