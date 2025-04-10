from django.db import models
from django.core.validators import (MinValueValidator, MaxValueValidator,
                                    FileExtensionValidator)
from django.contrib.auth.models import User

# Create your models here.


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="teacher/teachers/", null=True, blank=True)

    def __str__(self):
        return self.user.username


class Course(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150)
    duration = models.IntegerField(default=8, validators=[
        MinValueValidator(1),
        MaxValueValidator(12)
    ])

    def __str__(self):
        return self.name


class Lesson(models.Model):
    theme = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    text = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to="lesson/photos/", null=True, blank=True)
    video = models.FileField(upload_to="lesson/videos/", validators=[
        FileExtensionValidator(allowed_extensions=['mp4'])
    ], null=True, blank=True)
    views = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.theme