from rest_framework import serializers
from django.core.validators import (FileExtensionValidator)

from .models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        # fields = ['pk', 'name', 'duration']
        # exclude = ['slug']
        # read_only_fields = ['pk']


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        read_only_fields = ['views']
        depth = 3



    # class CourseSerializer(serializers.Serializer):
#     pk = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=150)
#     duration = serializers.IntegerField(max_value=12, min_value=1, default=8)


# class LessonSerializer(serializers.Serializer):
#     pk = serializers.IntegerField(read_only=True)
#     slug = serializers.SlugField()
#     theme = serializers.CharField(max_length=250)
#     text = serializers.CharField(required=False)
#     photo = serializers.ImageField(required=False)
#     video = serializers.FileField(required=False, validators=[
#         FileExtensionValidator(["mp4"])
#     ])
#     course_id = serializers.IntegerField()
#     teacher_id = serializers.IntegerField()
